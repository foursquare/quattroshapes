#!/usr/bin/env python
import sys
from time import time
from datetime import timedelta

import math
import numpy

from psycopg2 import connect
from optparse import OptionParser

from itertools import groupby

# Database details
user_name = ''
database_name = ''
table_name = ''
adjacency_db_table_name = ''
place_type = ''
search_buffer = 0.2

# Database connection using psycopg2
db = None
cur = None

chatty = False


parser = OptionParser(usage="""%prog [options]

For all places, find their photos and calculate if each photo is range in or an outlier.""")

parser.add_option('-u', '-U', '--db_user_name', dest='db_user_name', default='foursquare',
                  help='Name of Postgres user to connect as.')

parser.add_option('-d', '--db_name', dest='db_name', default='foursquare',
                  help='Name of Postgres database to connect to.')

parser.add_option('-t', '--db_table_name', dest='db_table_name', default='geoplanet_places',
                  help='Name of table in Postgres database.')

parser.add_option('-a', '--adjacency_db_table_name', dest='adjacency_db_table_name', default='geoplanet_adjacencies',
                  help='Name of table in Postgres database.')

parser.add_option('-p', '--place_type', dest='place_type', default='Town',
                  help='Valid WOE placetypes are County, LocalAdmin, Town.')

parser.add_option('-c', '--compare_place_type', dest='compare_place_type', default='County',
                  help='Valid WOE placetypes are County, LocalAdmin, Town.')

parser.add_option('-b', '--search_buffer', dest='search_buffer', default=0.1,
                  help='Distance in map units (usually meters or decimal degrees) from the source place to the reference places to limit search to immediate neighborhood.')


(options, args) = parser.parse_args()

    
def evaluate_neighbors( woe_id ):    
    # Where is this place?
    cur.execute("""
        SELECT 
            ST_ASTEXT(the_geom),
            woe_adm2
        FROM 
            """ + db_table_name + """
        WHERE 
            woe_id = (%s)""", (woe_id,))
    
    this_woe_geom, reference_parent_id = cur.fetchone()
    
    # What does GeoPlanet say about this place's neighbors?
    cur.execute("""
        SELECT 
            neighbor_woe_id
        FROM 
            """ + adjacency_db_table_name + """
        WHERE 
            place_woe_id = (%s)""", (woe_id,))
    
    neighbors_list_raw = cur.fetchall()
    
    neighbors_list = []
    
    #tupples from fetch to basic list of ints
    for n in neighbors_list_raw:
        neighbors_list.append(n[0])
    
    #print "neighbors_list", neighbors_list
    
    # How many reference places should exist?
    neighbors_total = len(neighbors_list)
    
    limit = 20
    
    # Get all places within <search_buffer> meters of this place point for places of like type. 
    cur.execute("""
        select      woe_id,
                    {4}
        from        {0}
        where       ST_DWITHIN(
                        the_geom,
                        ST_SETSRID(ST_GEOMFROMTEXT('{1}'),4326),
                        {2}
                    )
        and         placetype = '{3}'
        and         woe_id != {6}
        order by    ST_DISTANCE(
                        the_geom,
                        ST_SETSRID(ST_GEOMFROMTEXT('{1}'),4326)
                    ) asc
        LIMIT {5};""".format(db_table_name, this_woe_geom, search_buffer, place_type, compare_place_type, limit, woe_id))

    ref_places = cur.fetchall()

    #Track how many spatial neighbors match expected database neighbors
    counter = 0
    parent_cohort_counter = 0
    
    parent_woes = []
    
    ref_places_len = len(ref_places)
    
    # Going nearest to farthest from the source point.
    for ref_place in ref_places:
        ref_woe_id, ref_parent_id = ref_place
        
        if ref_woe_id in neighbors_list:
            counter = counter + 1

        parent_woes.append( ref_parent_id )
        
    parent_cohort_counter = parent_woes.count(reference_parent_id)
    
    #print parent_woes, parent_cohort_counter, reference_parent_id

    accuracy = 'unknown'

    if neighbors_total > 0 and (counter is 0 and parent_cohort_counter is 0):
        accuracy = 'bad'

    if parent_cohort_counter > 1:
        if neighbors_total is 0:
            accuracy = 'good parents, null neighbors'
        else:
            accuracy = 'good parents'

    if counter > 0:
        accuracy = 'good neighbors'

    if counter > 0 and parent_cohort_counter > 0:
        accuracy = 'good neighbors and parents'

        if neighbors_total is not 0:
            fraction = float(counter) / neighbors_total

        if ref_places_len is not 0:
            parent_fraction = float(parent_cohort_counter) / ref_places_len
        
        if counter > 4 and fraction > .75 and parent_cohort_counter > 4 and parent_fraction > .75:
            accuracy = 'great neighbors and parents'
        
    #print '\t', accuracy

    #return (neighbors_total, counter, fraction, parent_cohort_counter, parent_fraction)
    
    return accuracy

def main():
    #Get all the places of that placetype
    cur.execute("""
        SELECT 
            woe_id, name
        FROM """ + db_table_name + 
        """ WHERE placetype = (%s) 
            AND accuracy = 'geonames match great'
            AND spatial_accuracy IS NULL
        ORDER BY woe_id
        LIMIT 37000
        OFFSET (37000 * 0)
        """, (place_type,))
        #""" WHERE placetype = (%s) AND photos = 0""", (place_type,))
    
    places = cur.fetchall()
    
    print 'Evaluating %s places of type %s for parent-type %s...' % (len(places), place_type, compare_place_type)
    
    total_places = len(places)
    counter = 0
    for place in places:
        counter += 1
        
        woe_id, name = place
    
        if total_places > 1000:
            if counter % 100 == 0:
                print '%s of %s: %s (%s)' % (counter, total_places, name, woe_id)
        else:
            print '%s of %s: %s (%s)' % (counter, total_places, name, woe_id)
    
        accuracy = evaluate_neighbors( woe_id )
        
        if total_places > 1000:
            if counter % 100 == 0:
                print '\t%s' % (accuracy,)
        else:
            print '\t%s' % (accuracy,)
            
        cur.execute("""
            UPDATE 
                geoplanet_places
            SET 
                spatial_accuracy = '""" + accuracy + """'
            WHERE 
                woe_id = """ + str(woe_id) )

        db.commit()
                
    return total_places

if __name__ == '__main__':
    app_time_start = time()

    db_user_name = options.db_user_name
    
    db_name = options.db_name
    db_table_name = options.db_table_name
    adjacency_db_table_name = options.adjacency_db_table_name
    place_type = options.place_type
    compare_place_type = options.compare_place_type
    search_buffer = options.search_buffer
    
    #woe_locality | woe_lau  | woe_adm2 | woe_adm1 | woe_adm0
    # Normalize the WOE placetype and determine which table to read photos from
    if place_type == 'Admin1' or place_type == 'State':
        place_type = 'State'
    elif place_type == 'Admin2' or place_type == 'County':
        place_type = 'County'
    elif place_type == 'Admin3' or place_type == 'LocalAdmin' or place_type == 'LAU':
        place_type = 'LocalAdmin'
    elif place_type == 'Town' or place_type == 'Locality':
        place_type = 'Town'
    elif place_type == 'Suburb' or place_type == 'Neighborhood':
        place_type = 'Suburb'
    
    if compare_place_type == 'Admin1' or compare_place_type == 'State':
        compare_place_type = 'woe_adm1'
    elif compare_place_type == 'Admin2' or compare_place_type == 'County':
        compare_place_type = 'woe_adm2'
    elif compare_place_type == 'Admin3' or compare_place_type == 'LocalAdmin' or compare_place_type == 'LAU':
        compare_place_type = 'woe_lau'
    else:
        print "Only Admin1, Admin2, and LocalAdmin are valid comparisions"
        exit (0)
    
    print "Evaluating", place_type, "..."
    
    # Connect to the database        
    db = connect(user=db_user_name, database=db_name)
    cur = db.cursor()
    
    total_places = main()
        
    app_time_end = time()
    time_display = str( timedelta(seconds=(app_time_end - app_time_start)))
    app_time_total_minutes = round((app_time_end - app_time_start) / 60, 1)
    if app_time_total_minutes > 1: 
        ppm = round(float(total_places) / app_time_total_minutes)
    else:
        ppm = total_places
    
    print 'Caluclated %d bounds in %s (%s places per minute)' % (total_places, time_display, ppm)    