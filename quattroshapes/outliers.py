#!/usr/bin/env python
import sys
from time import time

import math
import numpy

from psycopg2 import connect
from optparse import OptionParser

# Outlier storage
MEDIAN_THRESHOLD = 5.0

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



def median_distances(pts, aggregate=numpy.median):
    median = (numpy.median([pt[0] for pt in pts]),
              numpy.median([pt[1] for pt in pts]))
    distances = []
    for pt in pts:
        dist = math.sqrt(((median[0]-pt[0])*math.cos(median[1]*math.pi/180.0))**2+(median[1]-pt[1])**2)
        distances.append((dist, pt))

    median_dist = aggregate([dist for dist, pt in distances])
    return (median_dist, distances, median)
    
def mean_distances(photos):
    return median_distances(photos, numpy.mean)

def load_photos( woe_id, place_filter={} ):
    cur.execute("""
        SELECT 
            longitude, latitude, photo_id
        FROM """ + db_photos + """
        WHERE woe_id = (%s)
        """, (woe_id,))
    
    photos = cur.fetchall()

    #print '\t', len(photos), 'photos'
    
    return photos

def discard_outliers(photos, threshold=MEDIAN_THRESHOLD):
    count = 0
    discarded = 0
    result = {}
    
    total_photos = len(photos)
    
    if chatty: 
        print '\tComputing outliers...'
    
    median_dist, distances, median = median_distances( photos )
    
    if chatty: 
        print '\tmedian_dist:', median_dist
    
    if median_dist > 0:
        keep = [pt for dist, pt in distances if dist < median_dist * threshold]
        discarded += total_photos - len(keep)

        if chatty: 
            print '\t%d photos discarded of %d total' % (discarded, total_photos)
        
        return (keep, median, discarded)
    else:
        if chatty: 
            print '\t%d photos discarded of %d total (dense cluster)' % (0, total_photos)

        return (photos, median, 0)

def get_bbox_for_place( photos ):
    bbox = [180, 90, -180, -90]
    
    for pt in photos:
        for i in range(4):
            bbox[i] = min(bbox[i], pt[i%2]) if i<2 else max(bbox[i], pt[i%2])
            
    return bbox

def main():
    #Get all the places of that placetype
    cur.execute("""
        SELECT 
            woe_id, name
        FROM """ + db_table_name + 
        """ WHERE placetype = (%s)""", (place_type,))
    
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
        
        if len(photos) > 0:
            photos, median, discarded = discard_outliers( photos )
        
            bbox = get_bbox_for_place( photos )
            
            #print '\t%s: %s %s, %s %s' % (woe_id, bbox[0], bbox[1], bbox[2], bbox[3])
            #print '\t%s, %s' % (median[0], median[1])
            
            #Store result
            # Clear out the table first!
            #   DELETE FROM db_photos_clean;
            for photo in photos:            
                cur.execute("""
                    INSERT 
                    INTO """ + db_photos_clean + """
                        (photo_id, woe_id, longitude, latitude)
                    VALUES 
                        (""" + str(photo[2]) + """,""" 
                             + str(woe_id) + """,""" 
                             + str(photo[0]) + """,""" 
                             + str(photo[1]) + """)""" )

                db.commit()
                
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
                    photos = """ + str(len(photos)) + """,
                    outliers = """ + str(discarded) + """
                WHERE gp.woe_id = """ + str(woe_id) )

            db.commit()

        #if counter > 1000:
        #    break


if __name__ == '__main__':
    app_time_start = time()

    db_user_name = options.db_user_name
    
    db_name = options.db_name
    db_table_name = options.db_table_name
    place_type = options.place_type
    
    # Normalize the WOE placetype and determine which table to read photos from
    if place_type == 'Country':
        db_photos = 'flickr_adm0_data'
    elif place_type == 'Admin' or place_type == 'State':
        place_type = 'State'
        db_photos = 'flickr_adm1_data'
    elif place_type == 'Admin2' or place_type == 'County':
        place_type = 'County'
        db_photos = 'flickr_adm2_data'
    elif place_type == 'Admin3' or place_type == 'LocalAdmin' or place_type == 'LAU':
        print 'Admin3 is not supported at this time.'
        place_type = 'LocalAdmin'
    elif place_type == 'Town' or place_type == 'Locality':
        place_type = 'Town'
        db_photos = 'flickr_locality_data'
    elif place_type == 'Suburb' or place_type == 'Neighborhood':
        place_type = 'Suburb'
        db_photos = 'flickr_neighborhood_data'
        
    db_photos_clean = db_photos + '_clean'

    # Connect to the database        
    db = connect(user=db_user_name, database=db_name)
    cur = db.cursor()
    
    main()
    
    app_time_end = time()
    app_time_total_minutes = round((app_time_end - app_time_start) / 1000 / 60, 1)
    
    print 'Outliers calculated in %s minutes.' % (app_time_total_minutes)