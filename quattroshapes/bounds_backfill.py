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

parser.add_option('-p', '--place_type', dest='place_type', default='Locality',
                  help='Valid WOE placetypes are Country, State, County, LocalAdmin, Town, and Suburb.')

(options, args) = parser.parse_args()



def load_photos( woe_id, place_filter={} ):
    if place_type == 'Country':
        cur.execute("""
            SELECT 
                longitude, latitude, photo_id
            FROM """ + db_photos + """
            WHERE woe_adm0 = %s
            """, (woe_id,))
    elif place_type == 'State':
        cur.execute("""
            SELECT 
                longitude, latitude, photo_id
            FROM """ + db_photos + """
            WHERE woe_adm1 = %s
            """, (woe_id,))
    elif place_type == 'County':
        cur.execute("""
            SELECT 
                longitude, latitude, photo_id
            FROM """ + db_photos + """
            WHERE woe_adm2 = %s
            """, (woe_id,))
    elif place_type == 'LocalAdmin':
        cur.execute("""
            SELECT 
                longitude, latitude, photo_id
            FROM """ + db_photos + """
            WHERE woe_lau = %s
            """, (woe_id,))
    elif place_type == 'Town':
        cur.execute("""
            SELECT 
                longitude, latitude, photo_id
            FROM """ + db_photos + """
            WHERE woe_locality = %s
            """, (woe_id,))
    elif place_type == 'Suburb':
        cur.execute("""
            SELECT 
                longitude, latitude, photo_id
            FROM """ + db_photos + """
            WHERE woe_locality = %s
            """, (woe_id,))
    
    photos = cur.fetchall()
    
    #print '\t', len(photos), 'photos'
    
    return photos
    
def load_bbox_fallback( woe_id, place_filter={} ):
    
    bbox = [1, 1, -1, -1]
    median = (0,0)
    accuracy = 'flickr null island'
    
    nesting_levels = 10
    level = 0 
    
    while level < nesting_levels:
        level += 1
        
        cur.execute("""
            SELECT 
                placetype, parent_id
            FROM 
                """ + db_table_name + """
            WHERE 
                woe_id = (%s);""", (woe_id,))
            
        try:
            placetype, parent_id = cur.fetchone()
        except:
            return (bbox, median, accuracy)
        
        #print placetype, parent_id
        
        cur.execute("""
            SELECT 
                x_min, y_min, x_max, y_max, centroid_lon, centroid_lat
            FROM """ + db_table_name + 
            """ WHERE woe_id = (%s)""", (parent_id,))

        try:
            x_min, y_min, x_max, y_max, centroid_lon, centroid_lat = cur.fetchone()
            #don't return junk
            if x_min is None or centroid_lon is None:
                return (bbox, median, accuracy)
            #print x_min, y_min, x_max, y_max, centroid_lon, centroid_lat
            break
        except:
            return (bbox, median, accuracy)
            
        #set us up for the next loop
        woe_id = parent_id

    #print '\t', len(photos), 'photos'
    
    bbox = [x_max, y_max, x_min, y_min]
    median = (centroid_lon, centroid_lat)

    try:
        cur.execute("""
            SELECT 
                placetype
            FROM 
                """ + db_table_name + """
            WHERE 
                woe_id = (%s);""", (parent_id,))
        
        accuracy_place_type = cur.fetchone()
    except:
        return (bbox, median, accuracy)
    
    if accuracy_place_type[0] == 'Town' or accuracy_place_type[0] == 'Suburb':
        accuracy = 'flickr aggreate ' + accuracy_place_type[0]
    else:
        accuracy = 'flickr parent ' + accuracy_place_type[0]
    
    return (bbox, median, accuracy)

def get_bbox_for_place( photos ):
    bbox = [180, 90, -180, -90]
    
    for pt in photos:
        for i in range(4):
            bbox[i] = min(bbox[i], pt[i%2]) if i<2 else max(bbox[i], pt[i%2])

    median = (numpy.median([pt[0] for pt in photos]),
              numpy.median([pt[1] for pt in photos]))

    return (bbox, median)

def main():
    #Get all the places of that placetype
    cur.execute("""
        SELECT 
            woe_id, name
        FROM """ + db_table_name + 
        """ WHERE placetype = (%s) AND photos IS NULL""", (place_type,))
        #""" WHERE placetype = (%s) AND photos = 0""", (place_type,))
    
    places = cur.fetchall()
    
    print 'Evaluating %s places of type %s...' % (len(places), place_type)
    
    total_places = len(places)
    counter = 0
    for place in places:
        counter += 1
        
        woe_id, name = place
    
        if total_places > 10000:
            if counter % 1000 == 0:
                print '%s of %s: %s (%s)' % (counter, total_places, name, woe_id)
        else:
            print '%s of %s: %s (%s)' % (counter, total_places, name, woe_id)
    
        photos = load_photos( woe_id )
    
        total_photos = len(photos)
                
        if total_photos is None or total_photos == 0:
            bbox, median, accuracy = load_bbox_fallback( woe_id )
        else:
            bbox, median = get_bbox_for_place( photos )
            accuracy = 'flickr proxy locality-suburb'
        
        if total_places > 10000:
            if counter % 1000 == 0:
                print '\t%s: %s %s, %s %s' % (woe_id, bbox[0], bbox[1], bbox[2], bbox[3])
                print '\t%s, %s' % (median[0], median[1])
                print '\t%s' % (accuracy,)
        else:
            print '\t%s: %s %s, %s %s' % (woe_id, bbox[0], bbox[1], bbox[2], bbox[3])
            print '\t%s, %s' % (median[0], median[1])
            print '\t%s' % (accuracy,)
        
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
                photos = -""" + str(len(photos)) + """,
                accuracy = '""" + accuracy + """'
            WHERE gp.woe_id = """ + str(woe_id) )

        db.commit()
                
    return total_places

if __name__ == '__main__':
    app_time_start = time()

    db_user_name = options.db_user_name
    
    db_name = options.db_name
    db_table_name = options.db_table_name
    place_type = options.place_type
    
    #woe_locality | woe_lau  | woe_adm2 | woe_adm1 | woe_adm0
    # Normalize the WOE placetype and determine which table to read photos from
    if place_type == 'Country':
        search_place_type = 'woe_adm0'
        db_photos = 'flickr_merged_data'
    elif place_type == 'Admin' or place_type == 'State':
        search_place_type = 'woe_adm1'
        place_type = 'State'
        db_photos = 'flickr_merged_data'
    elif place_type == 'Admin2' or place_type == 'County':
        search_place_type = 'woe_adm2'
        place_type = 'County'
        db_photos = 'flickr_merged_data'
    elif place_type == 'Admin3' or place_type == 'LocalAdmin' or place_type == 'LAU':
        search_place_type = 'woe_lau'
        #print 'Admin3 is not supported at this time.'
        place_type = 'LocalAdmin'
        db_photos = 'flickr_merged_data'
    elif place_type == 'Town' or place_type == 'Locality':
        search_place_type = 'woe_locality'
        place_type = 'Town'
        db_photos = 'flickr_merged_data'
    elif place_type == 'Suburb' or place_type == 'Neighborhood':
        search_place_type = 'woe_locality'
        place_type = 'Suburb'
        db_photos = 'flickr_merged_data'
    
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