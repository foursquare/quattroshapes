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

# Explicate write and read database settings
db_write_results = ''
db_write_unique_id = ''
db_read_unique_id = ''
db_read_placetype = ''

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



def load_photos( unique_id, place_filter={} ):
    cur.execute("""
        SELECT 
            longitude, latitude
        FROM 
            """ + db_photos + """
        WHERE 
            """ + db_read_unique_id + """ = """ + str(unique_id) )
    
    photos = cur.fetchall()
    
    #print '\t', len(photos), 'photos'
    
    return photos


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
            """ + db_write_unique_id + """, name
        FROM """ + db_table_name ) #+ 
#        """ WHERE """ + db_read_placetype + """ = '""" + place_type + """'""")
    
    places = cur.fetchall()
    
    print 'Evaluating %s places of type %s...' % (len(places), place_type)
    
    total_places = len(places)
    counter = 0
    for place in places:
        counter += 1
        
        unique_id, name = place
    
        if total_places > 10000:
            if counter % 1000 == 0:
                print '%s of %s: %s (%s)' % (counter, total_places, name, unique_id)
        else:
            print '%s of %s: %s (%s)' % (counter, total_places, name, unique_id)
    
        photos = load_photos( unique_id )
        total_photos = len(photos)

        if total_places > 10000:
            if counter % 1000 == 0:
                print '\t', total_photos, 'photos'
        else:
            print '\t', total_photos, 'photos'
            
        if total_photos > 0:
            bbox, median = get_bbox_for_place( photos )
            
            #print '\t%s: %s %s, %s %s' % (unique_id, bbox[0], bbox[1], bbox[2], bbox[3])
            #print '\t%s, %s' % (median[0], median[1])
            
            cur.execute("""
                UPDATE 
                    """ + db_write_results + """ gp
                SET 
                    centroid_lon = """ + str(median[0]) + """,
                    centroid_lat = """ + str(median[1]) + """,
                    x_min = """ + str(bbox[0]) + """,
                    y_min = """ + str(bbox[1]) + """,
                    x_max = """ + str(bbox[2]) + """,
                    y_max = """ + str(bbox[3]) + """,
                    photos = """ + str(len(photos)) + """
                WHERE gp.""" + db_write_unique_id + """ = """ + str(unique_id) )

            db.commit()
                
    return total_places

if __name__ == '__main__':
    app_time_start = time()

    db_user_name = options.db_user_name
    
    db_name = options.db_name
    db_table_name = options.db_table_name
    place_type = options.place_type
    
    # Normalize the WOE placetype and determine which table to read photos from
    if place_type == 'Country':
        db_photos = 'flickr_adm0_data'
        db_write_results = 'geoplanet_places'
        db_write_unique_id = 'woe_id'
        db_read_unique_id = 'woe_id'
        db_read_placetype = 'placetype'
    elif place_type == 'Admin' or place_type == 'State':
        place_type = 'State'
        db_photos = 'flickr_adm1_data'
        db_write_results = 'geoplanet_places'
        db_write_unique_id = 'woe_id'
        db_read_unique_id = 'woe_id'
        db_read_placetype = 'placetype'
    elif place_type == 'Admin2' or place_type == 'County':
        place_type = 'County'
        db_photos = 'flickr_adm2_data'
        db_write_results = 'geoplanet_places'
        db_write_unique_id = 'woe_id'
        db_read_unique_id = 'woe_id'
        db_read_placetype = 'placetype'
    elif place_type == 'Admin3' or place_type == 'LocalAdmin' or place_type == 'LAU':
        print 'Admin3 is not supported at this time.'
        place_type = 'LocalAdmin'
        db_write_results = 'geoplanet_places'
        db_write_unique_id = 'woe_id'
        db_read_unique_id = 'woe_id'
        db_read_placetype = 'placetype'
    elif place_type == 'Town' or place_type == 'Locality':
        place_type = 'Town'
        db_photos = 'flickr_locality_data'
        db_write_results = 'geoplanet_places'
        db_write_unique_id = 'woe_id'
        db_read_unique_id = 'woe_id'
        db_read_placetype = 'placetype'
    elif place_type == 'Suburb' or place_type == 'Neighborhood':
        place_type = 'Suburb'
        db_photos = 'flickr_neighborhood_data'
        db_write_results = 'geoplanet_places'
        db_write_unique_id = 'woe_id'
        db_read_unique_id = 'woe_id'
        db_read_placetype = 'placetype'
    elif place_type == 'Geoname Locality':
        place_type = 'PPL'
        db_photos = 'checkins'
        db_write_results = 'geoname'
        db_write_unique_id = 'geonameid'
        db_read_unique_id = 'geoname_id'
        db_read_placetype = 'fcode'
    elif place_type == 'Geoname Population':
        place_type = 'P'
        db_photos = 'checkins'
        db_write_results = 'geoname'
        db_write_unique_id = 'geonameid'
        db_read_unique_id = 'geoname_id'
        db_read_placetype = 'fclass'
    elif place_type == 'Geoname Admin':
        place_type = 'A'
        db_photos = 'checkins'
        db_write_results = 'geoname'
        db_write_unique_id = 'geonameid'
        db_read_unique_id = 'geoname_id'
        db_read_placetype = 'fclass'
    
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