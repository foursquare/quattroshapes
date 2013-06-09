#!/usr/bin/env python
import sys
from time import time
from datetime import timedelta

import math
import numpy

from psycopg2 import connect
from optparse import OptionParser

# Database details
user_name = ''
database_name = ''
table_name = ''
adjacency_db_table_name = ''
place_type = ''
# Assumed the photos table is stored in the same database as geoplanet
db_photos = ''
db_photos_clean = ''

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

parser.add_option('-p', '--place_type', dest='place_type', default='County',
                  help='Valid WOE placetypes are County, LocalAdmin, Town.')

(options, args) = parser.parse_args()

    
def load_bbox_fallback( woe_id, orig_accuracy, place_filter={} ):
    
    bbox = [1, 1, -1, -1]
    median = (0,0)
    centroids = [median]
    accuracy = orig_accuracy
    
    cur.execute("""
        SELECT 
            neighbor_woe_id
        FROM 
            """ + adjacency_db_table_name + """
        WHERE 
            place_woe_id = (%s)""", (woe_id,))
    
    neighbors_list = cur.fetchall()
       
    if len(neighbors_list) > 0:                
        counter = 0
        accuracy_place_type = 'null'
    
        centroids = []
        
        for neighbor in neighbors_list:
            neighbor_id = neighbor[0]
            try:            
                cur.execute("""
                    SELECT 
                        placetype, woe_id, x_min, y_min, x_max, y_max, centroid_lon, centroid_lat
                    FROM 
                        """ + db_table_name + """
                    WHERE 
                        woe_id = (%s)
                        AND accuracy IN ('flickr aggregate Suburb','flickr aggregate Town', 'flickr median', 'geonames match', 'geonames match round 2')
                        AND gn_matchaccuracy NOT IN ('unknown', 'twofish bad checkins extent')
                        AND gn_matchaccuracy IS NOT NULL;""", (neighbor_id,))


                neighbor_details = cur.fetchone()
                #print '\t', len(children), 'children places'

                placetype, woe_id, x_min, y_min, x_max, y_max, centroid_lon, centroid_lat = neighbor_details
        
                #print x_min, y_min, x_max, y_max, centroid_lon, centroid_lat

                #don't return junk
                if x_min is None or centroid_lon is None:
                    return (bbox, median, accuracy)

                if counter is 0:
                    bbox = [x_max, y_max, x_min, y_min]
                    accuracy_place_type = placetype
                else:
                    bbox[0] = min(bbox[0], x_min)
                    bbox[1] = min(bbox[1], y_min)
                    bbox[2] = max(bbox[2], x_max)
                    bbox[3] = max(bbox[3], y_max)
                                    
                centroids.append( (centroid_lon,centroid_lat) )
        
                counter = counter + 1
            except:
                return (bbox, median, accuracy)

        # bbox is already set
        median = (numpy.median([pt[0] for pt in centroids]),
                  numpy.median([pt[1] for pt in centroids]))
        accuracy = 'flickr neighbor ' + accuracy_place_type
        
    return (bbox, median, accuracy)


def main():
    #Get all the places of that placetype
    cur.execute("""
        SELECT 
            woe_id, name, accuracy
        FROM """ + db_table_name + 
        """ WHERE placetype = (%s) 
            AND accuracy IN ('flickr parent State','flickr parent Country', 'flickr parent County', 'flickr parent LocalAdmin', 'flickr null island', 'flickr proxy locality-suburb') 
        """, (place_type,))
        #""" WHERE placetype = (%s) AND photos = 0""", (place_type,))
    
    places = cur.fetchall()
    
    print 'Evaluating %s places of type %s...' % (len(places), place_type)
    
    total_places = len(places)
    counter = 0
    for place in places:
        counter += 1
        
        woe_id, name, orig_accuracy = place
    
        if total_places > 1000:
            if counter % 100 == 0:
                print '%s of %s: %s (%s)' % (counter, total_places, name, woe_id)
        else:
            print '%s of %s: %s (%s)' % (counter, total_places, name, woe_id)
    
        bbox, median, accuracy = load_bbox_fallback( woe_id, orig_accuracy )
        
        if total_places > 1000:
            if counter % 100 == 0:
                print '\t%s: %s %s, %s %s' % (woe_id, bbox[0], bbox[1], bbox[2], bbox[3])
                print '\t%s, %s' % (median[0], median[1])
                print '\t%s' % (accuracy,)
        else:
            print '\t%s: %s %s, %s %s' % (woe_id, bbox[0], bbox[1], bbox[2], bbox[3])
            print '\t%s, %s' % (median[0], median[1])
            print '\t%s' % (accuracy,)
            
        if orig_accuracy != accuracy:
            cur.execute("""
                UPDATE 
                    geoplanet_places gp
                SET 
                    centroid_lon = """ + str(median[0]) + """,
                    centroid_lat = """ + str(median[1]) + """,
                    x_min = """ + str(bbox[0]) + """,
                    y_min = """ + str(bbox[1]) + """,
                    x_max = """ + str(bbox[2]) + """,
                    y_max = """ + str(bbox[3]) + """,
                    accuracy = '""" + accuracy + """'
                WHERE gp.woe_id = """ + str(woe_id) )

            db.commit()
                
    return total_places

if __name__ == '__main__':
    app_time_start = time()

    db_user_name = options.db_user_name
    
    db_name = options.db_name
    db_table_name = options.db_table_name
    adjacency_db_table_name = options.adjacency_db_table_name
    place_type = options.place_type
    
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