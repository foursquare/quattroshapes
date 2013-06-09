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

# Assumed the photos table is stored in the same database as geoplanet
db_photos = ''
db_photos_clean = ''

# Explicate write and read database settings
db_write_results = ''
db_write_unique_id = ''
db_read_unique_id = ''

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

parser.add_option('-t', '--db_table_name', dest='db_table_name', default='quatroshapes_extras',
                  help='Name of table in Postgres database.')

parser.add_option('-c', '--count', dest='count', default=1,
                  help='How many neighbors must match to NOT be an outlier.')

(options, args) = parser.parse_args()



def load_neighbors( wkt, place_filter={} ):
    cur.execute("""
        SELECT 
            """ + db_write_unique_id + """ as id,
            COUNT(""" + db_write_unique_id + """) as neighbors
        FROM 
            """ + db_table_name + """
        WHERE 
            ST_Touches( poly_geom, ST_GeomFromText('""" + wkt + """', 4326) )
        GROUP BY 
            """ + db_write_unique_id + """
        ORDER BY 
            neighbors DESC;
        """)
    
    neighbors = cur.fetchall()
    #print '\t', len(neighbors), 'neighbors'
    
    return neighbors

def main():
    #Get all the places of that placetype
    cur.execute("""
        SELECT 
            """ + db_write_unique_id + """, name, zoom, row, col,
            ST_AsText( poly_geom ) as wkt
        FROM """ + db_table_name )
    
    places = cur.fetchall()
    
    print 'Evaluating %s places...' % (len(places),)
    
    total_places = len(places)
    counter = 0
    
    for place in places:
        counter += 1
        
        unique_id, name, zoom, row, col, wkt = place
    
        if total_places > 10000:
            if counter % 1000 == 0:
                print '%s of %s: %s (%s) at %s/%s/%s' % (counter, total_places, name, unique_id, zoom, row, col)
        else:
            print '%s of %s: %s (%s) at %s/%s/%s' % (counter, total_places, name, unique_id, zoom, row, col)
    
        neighbors = load_neighbors( wkt )
        total_neighbors = len(neighbors)
            
        if total_neighbors > 0:
            
            # is at least one of the neighbors of the same id? if not:
            outlier = True
            c = 0
            
            #This should always be length of 8
            for n in neighbors:
                if n[0] == unique_id:
                    c = c + 1
                    
            if c >= count_threshold:
                outlier = False
            
            if outlier:
                cur.execute("""
                    UPDATE 
                        """ + db_write_results + """
                    SET 
                        """ + db_write_unique_id + """ = """ + str(neighbors[0][0]) + """
                    WHERE 
                        zoom = """ + str(zoom) + """ AND 
                        row = """ + str(row) + """ AND 
                        col = """ + str(col) )
                db.commit()
                
    return total_places

if __name__ == '__main__':
    app_time_start = time()

    db_user_name = options.db_user_name
    
    db_name = options.db_name
    db_table_name = options.db_table_name
    count_threshold = options.count
    
    db_photos = 'quatroshapes_extras'
    db_write_results = 'quatroshapes_extras'
    db_write_unique_id = 'woe_id'
    db_read_unique_id = 'woe_id'
        
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