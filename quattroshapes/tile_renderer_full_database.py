import csv, sys
from sys import argv, stdout, stderr
from subprocess import Popen
from os import stat, unlink

try:
    from json import JSONEncoder, loads as json_loads
except ImportError:
    from simplejson import JSONEncoder, loads as json_loads

import json

from stat import ST_SIZE
from time import time
from re import sub

from math import pow, log, floor, ceil

from psycopg2 import connect
#http://initd.org/psycopg/docs/usage.html#unicode-handling
import psycopg2.extensions

from PIL.ImageDraw import ImageDraw
from PIL import Image

from ModestMaps.Core import Coordinate
from ModestMaps.Tiles import toMicrosoft
from ModestMaps.Core import Coordinate
from ModestMaps.OpenStreetMap import Provider

from TileStache.Core import KnownUnknown
from TileStache.Vector import VectorResponse

from tilestacheexceptions import NothingMoreToSeeHere
from tilestacheexceptions import NothingToSeeHere

osm = Provider()

colors = [
    (0,0,0),
    (8,29,88),
    (37,52,148),
    (34,94,168),
    (29,145,192),
    (65,182,196),
    (127,205,187),
    (199,233,180),
    (237,248,177),
    (255,255,217)
    ]


cell_size = 8
min_size = 1
max_size = 1000000
log_base = (max_size - min_size) ** (1./len(colors))
method = "" 

fat_pixel_count = 32

input_field = ""
woe_field = ""

db_user_name = ""
db_read_name = ""
db_read_table_name = ""
db_write_name = ""
db_write_table_name = ""
        
db = None
cur = None


def size_color(size):
    """ Return an interpolated color for a given byte size.
    """
    index = 0
    if size > 0:
        index = 1
    if size > 29:
        index = 2
    if size > 49:
        index = 3
    if size > 74:
        index = 4
    if size > 99:
        index = 5
    if size > 199:
        index = 6
    if size > 499:
        index = 7
    if size > 999:
        index = 8
    if size > 1999:
        index = 9

    if( index > len(colors) ):
        index = len(colors) - 1
    if( index < 0 ):
        index = 0
            
    low_index = int(index)
    high_index = low_index + 1
    
    high_mix = index - low_index
    low_mix = 1 - high_mix
    
    r1, g1, b1 = colors[low_index]

    try:
        r2, g2, b2 = colors[high_index]
    except IndexError:
        return colors[-1]
    
    return (int(r1 * low_mix + r2 * high_mix),
            int(g1 * low_mix + g2 * high_mix),
            int(b1 * low_mix + b2 * high_mix))
            

def size_color_log(size):
    """ Return an interpolated color for a given byte size.
    """
    try:
        index = log(size - min_size) / log(log_base)
        if( index > len(colors) ):
            index = len(colors) - 1
        if( index < 0 ):
            index = 0
    except ValueError:
        index = 0
    
    low_index = int(index)
    high_index = low_index + 1
    
    high_mix = index - low_index
    low_mix = 1 - high_mix
    
    r1, g1, b1 = colors[low_index]

    try:
        r2, g2, b2 = colors[high_index]
    except IndexError:
        return colors[-1]
    
    return (int(r1 * low_mix + r2 * high_mix),
            int(g1 * low_mix + g2 * high_mix),
            int(b1 * low_mix + b2 * high_mix))


def size_color_unique_id(unique_id=999999999):
    """ Return an interpolated color for a given byte size.
    """
    #r1 = size[-3:]
    #g1 = size[-6:-3]
    #b1 = size[-9:-6]
    
    red = (unique_id >> 16) & 0xff
    green = (unique_id >> 8) & 0xff
    blue = unique_id & 0xff
    
    try:
        red = int( float(red) / 1000 * 255)
        green = int( float(green) / 1000 * 255)
        blue = int( float(blue) / 1000 * 255)
        return (red,green,blue)
    except:
        return (255,255,255)
        
def count_votes( self, coord ):
    cood_start_time = time()
    
    #Defaults
    woe_id_0, woe_lau_0, woe_adm2_0, woe_adm1_0, woe_adm0_0, name_0, photo_count_0 = [-1,-1,-1,-1,-1,u"-1",-1]
    woe_id_1, name_1, photo_count_1 = [-1,u"-1",-1]
    #woe_id_2, name_2, photo_count_2 = [-1,u"-1",-1]
    #woe_id_3, name_3, photo_count_3 = [-1,u"-1",-1]
    #woe_id_4, name_4, photo_count_4 = [-1,u"-1",-1]

    ne = osm.coordinateLocation(coord.right())
    sw = osm.coordinateLocation(coord.down())

    #print "db_user_name:", self.db_user_name, " db_read_name: ", self.db_read_name
    #self.db = connect(user=self.db_user_name, database=self.db_read_name)
    #curs = self.db.cursor()

    curs = self.db.cursor()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, curs)

    curs.execute("""
        SELECT 
            """ + self.woe_field + """
        FROM """ + self.db_read_table_name + 
        """ WHERE photo_geom && ST_SetSRID(ST_MakeBox2D(ST_MakePoint((%s), (%s)), ST_MakePoint((%s), (%s))), 4326)
        LIMIT 1
    """, (sw.lon, sw.lat, ne.lon, ne.lat))

        #AND
        #""" + self.db_read_table_name + """.""" + self.woe_field + """ NOT IN (1648473,1625084,1646678,1642911,1645524,1649378) AND 
        #""" + self.db_read_table_name + """.level IN (7,14,35)

    
    # if we have photos
    # if we've done the subquads for a quad who's WOE is only itself (identity)
    # if we've got some photos but not a lot of photos and we're at the minimum viable zoom
    # or we're at the max zoom
    
    is_saveable = False
    
    # Do we want to do the min_zoom + 1 logic again?
    try:
        photo_count_total = curs.fetchone()[0]

        curs.execute("""
            SELECT 
                COUNT(""" + self.db_read_table_name + """.latitude) as "photos"
            FROM """ + self.db_read_table_name + 
            """ WHERE photo_geom && ST_SetSRID(ST_MakeBox2D(ST_MakePoint((%s), (%s)), ST_MakePoint((%s), (%s))), 4326)
        """, (sw.lon, sw.lat, ne.lon, ne.lat))
            
            #AND
            #""" + self.db_read_table_name + """.""" + self.woe_field + """ NOT IN (1648473,1625084,1646678,1642911,1645524,1649378) AND 
            #""" + self.db_read_table_name + """.level IN (7,14,35)

        photo_count_total = curs.fetchone()[0]

        if photo_count_total > 0:
            # Are we at the last requested zoom?
            if coord.zoom == self.max_zoom:
                is_saveable = True
            if (coord.zoom >= self.min_zoom): # and (photo_count_total <= self.min_size):
                is_saveable = True
    
    except:
        is_saveable = False
        photo_count_total = 0
    
    #print 'photo_count_total', photo_count_total, 'is_saveable', is_saveable

    if is_saveable:
        #sw = { 'lon':-123.04962, 'lat': 38.23387 }
        #ne = { 'lon': -121.81091, 'lat': 37.54675 }

        #SELECT
        #    flickr_locality_data.woe_id as "woe_id", geoplanet_places.name as "name", COUNT(flickr_locality_data.latitude) as "photos"
        #FROM
        #    flickr_locality_data, geoplanet_places
        #WHERE
        #    flickr_locality_data.woe_id = geoplanet_places.woe_id AND flickr_locality_data.photo_geom && ST_SetSRID(ST_MakeBox2D(ST_MakePoint(-123.04962, 38.23387), ST_MakePoint(-121.81091, 37.54675)), 4326) GROUP BY flickr_locality_data.woe_id, geoplanet_places.name ORDER BY photos DESC LIMIT 5;

        #curs.execute("""
            #SELECT 
            #    """ + self.db_read_table_name + """.""" + self.woe_field + """ as "woe_id", 
            #    """ + self.db_read_table_name + """.woe_lau as "woe_lau", 
            #    """ + self.db_read_table_name + """.woe_adm2 as "woe_adm2", 
            #    """ + self.db_read_table_name + """.woe_adm1 as "woe_adm1", 
            #    """ + self.db_read_table_name + """.woe_adm0 as "woe_adm0", 
            #    geoplanet_places.name as "name", 
            #    COUNT(""" + self.db_read_table_name + """.latitude) as "photos"
            #FROM
            #    """ + self.db_read_table_name + """, geoplanet_places
            #WHERE 
            #    """ + self.db_read_table_name + """.""" + self.woe_field + """ = geoplanet_places.woe_id AND 
            #    """ + self.db_read_table_name + """.photo_geom && 
            #    ST_SetSRID(ST_MakeBox2D(ST_MakePoint((%s), (%s)), ST_MakePoint((%s), (%s))), 4326)
            #GROUP BY 
            #    """ + self.db_read_table_name + """.""" + self.woe_field + """,
            #    """ + self.db_read_table_name + """.woe_lau,
            #    """ + self.db_read_table_name + """.woe_adm2,
            #    """ + self.db_read_table_name + """.woe_adm1,
            #    """ + self.db_read_table_name + """.woe_adm0,
            #    geoplanet_places.name ORDER BY photos DESC LIMIT 5;
            #""", (sw.lon, sw.lat, ne.lon, ne.lat))

        if self.woe_method == "woe":
            try:
                curs.execute("""
                    SELECT 
                        """ + self.db_read_table_name + """.""" + self.woe_field + """ as "woe_id", 
                        'lookup' as "name", 
                        COUNT(""" + self.db_read_table_name + """.latitude) as "photos"
                    FROM
                        """ + self.db_read_table_name + """
                    WHERE 
                        """ + self.db_read_table_name + """.photo_geom && 
                        ST_SetSRID(ST_MakeBox2D(ST_MakePoint((%s), (%s)), ST_MakePoint((%s), (%s))), 4326)
                    GROUP BY 
                        """ + self.db_read_table_name + """.""" + self.woe_field + """
                        ORDER BY photos DESC LIMIT 2;
                    """, (sw.lon, sw.lat, ne.lon, ne.lat))

                #curs.execute("""
                #    SELECT 
                #        """ + self.db_read_table_name + """.""" + self.woe_field + """ as "woe_id", 
                #        geoplanet_places.name as "name", 
                #        COUNT(""" + self.db_read_table_name + """.latitude) as "photos"
                #    FROM
                #        """ + self.db_read_table_name + """, geoplanet_places
                #    WHERE 
                #        """ + self.db_read_table_name + """.""" + self.woe_field + """ = geoplanet_places.woe_id AND 
                #        """ + self.db_read_table_name + """.photo_geom && 
                #        ST_SetSRID(ST_MakeBox2D(ST_MakePoint((%s), (%s)), ST_MakePoint((%s), (%s))), 4326)
                #    GROUP BY 
                #        """ + self.db_read_table_name + """.""" + self.woe_field + """,
                #        geoplanet_places.name ORDER BY photos DESC LIMIT 3;
                #    """, (sw.lon, sw.lat, ne.lon, ne.lat))

                #wait(dbs)
                #gevent_psycopg2.gevent_wait_callback(dbs)

                #result = curs.fetchall()
            except Exception, e:
                print e
                pass
        if self.woe_method == "checkins":
            woe_adm0_0 = -100
            try:
                curs.execute("""
                    SELECT 
                        """ + self.db_read_table_name + """.geoname_id as "woe_id", """
                        #""" + self.db_read_table_name + """.gn_placename as "name", 
                        """COUNT(""" + self.db_read_table_name + """.latitude) as "photos"
                    FROM
                        """ + self.db_read_table_name + """
                    WHERE 
                        """+ self.db_read_table_name + """.photo_geom && 
                        ST_SetSRID(ST_MakeBox2D(ST_MakePoint((%s), (%s)), ST_MakePoint((%s), (%s))), 4326)
                    GROUP BY 
                        """ + self.db_read_table_name + """.geoname_id
                    ORDER BY photos DESC LIMIT 2;
                    """, (sw.lon, sw.lat, ne.lon, ne.lat))

                        #""" + self.db_read_table_name + """.geoname_id NOT IN (1648473,1625084,1646678,1642911,1645524,1649378) AND 
                        #""" + self.db_read_table_name + """.level IN (7,14,35) AND 
                        #""" + self.db_read_table_name + """.gn_placename

                        #""" + self.db_read_table_name + """.level IN (8,9,10,12) AND 
                #wait(dbs)
                #gevent_psycopg2.gevent_wait_callback(dbs)

                #result = curs.fetchall()
            except Exception, e:
                print e
                pass
        
        try:
            #woe_id_0, woe_lau_0, woe_adm2_0, woe_adm1_0, woe_adm0_0, name_0, photo_count_0 = curs.fetchone()
            woe_id_0, photo_count_0 = curs.fetchone()
            name_0 = 'lookup'
        except Exception, e:
            #print 'oops', e
            woe_id_0, woe_lau_0, woe_adm2_0, woe_adm1_0, woe_adm0_0, name_0, photo_count_0 = [-1,-1,-1,-1,-1,u"-1",-1]
        
        try:
            #woe_id_1, woe_lau_1, woe_adm2_1, woe_adm1_1, woe_adm0_1, name_1, photo_count_1 = curs.fetchone()
            woe_id_1, photo_count_1 = curs.fetchone()
            name_1 = 'lookup'
        except Exception, e:
            #print 'oops', e
            woe_id_1, name_1, photo_count_1 = [-1,u"-1",-1]

        #try:
            #woe_id_2, woe_lau_2, woe_adm2_2, woe_adm1_2, woe_adm0_2, name_2, photo_count_2 = curs.fetchone()
        #    woe_id_2, name_2, photo_count_2 = curs.fetchone()
        #except:
        #    woe_id_2, name_2, photo_count_2 = [-1,u"-1",-1]

        #try:
            #woe_id_3, woe_lau_3, woe_adm2_3, woe_adm1_3, woe_adm0_3, name_3, photo_count_3 = curs.fetchone()
        #    woe_id_3, name_3, photo_count_3 = curs.fetchone()
        #except:
        #    woe_id_3, name_3, photo_count_3 = [-1,"-1",-1]

        #try:
            #woe_id_4, woe_lau_4, woe_adm2_4, woe_adm1_4, woe_adm0_4, name_4, photo_count_4 = curs.fetchone()
        #    woe_id_4, name_4, photo_count_4 = curs.fetchone()
        #except:
        #    woe_id_4, name_4, photo_count_4 = [-1,"-1",-1]
    
    
    if photo_count_0 > 0:
        margin = 1
    
    if photo_count_0 > 0 and photo_count_1 > 0:
        percent_0 = float(photo_count_0) / float(photo_count_total)
        percent_1 = float(photo_count_1) / float(photo_count_total)
        margin = percent_0 - percent_1
    
    if photo_count_1 == -1:
        margin = -1
        
    #print 'woe_id_0', woe_id_0, 'name_0', name_0, 'photo_count_0', photo_count_0
    
    result = {  "zoom":coord.zoom, 
                "column":coord.column, 
                "row":coord.row, 
                "time":(time() - cood_start_time), 
                "photo_count_total":photo_count_total, 
                "size":photo_count_total, # for compatibility
                "woe_id0":woe_id_0, 
                "woe_id0_lau":woe_lau_0, 
                "woe_id0_adm2":woe_adm2_0, 
                "woe_id0_adm1":woe_adm1_0, 
                "woe_id0_adm0":woe_adm0_0, 
                "name0":name_0, 
                "photo_count0":photo_count_0, 
                "margin0":margin
#                "woe_id1":woe_id_1, 
#                "name1":name_1, 
#                "photo_count1":photo_count_1, 
#                "woe_id2":woe_id_2, 
#                "name2":name_2, 
#                "photo_count2":photo_count_2 #, 
#                "woe_id3":woe_id_3, 
#                "name3":name_3, 
#                "photo_count3":photo_count_3, 
#                "woe_id4":woe_id_4, 
#                "name4":name_4, 
#                "photo_count4":photo_count_4
            }
            
    #print result

    return result

def getAdmins( woe_id ):
        # don't expect every coord to exist in the data file
        adm0_woe_id0, adm1_woe_id0, adm2_woe_id0, lau_woe_id0 = ["-1","-1","-1","-1"]
        
        #if neighborhood, then most often it's geoplanet_places.parent_id of that object?
        #SELECT
        #     geoplanet_admins.country_woe_id AS "country_woe_id", 
        #     geoplanet_admins.state_woe_id AS "state_woe_id", 
        #     geoplanet_admins.county_woe_id AS "county_woe_id", 
        #     geoplanet_admins.local_admin_woe_id AS "local_admin_woe_id"
        #FROM
        #    geoplanet_admins
        #WHERE
        #    geoplanet_admins.woe_id = 2355561;
                
        if db_read_table_name == 'flickr_neighborhood_data':
            cur.execute("""
                SELECT 
                    parent_id
                FROM
                    geoplanet_places
                WHERE 
                    woe_id = """ + str(woe_id) + """;""")
            locality = cur.fetchone()[0]
        else: 
            locality = woe_id
        
        locality = str(locality)

        if locality != "-1":
            cur.execute("""
                SELECT 
                    geoplanet_admins.country_woe_id,
                    geoplanet_admins.state_woe_id,
                    geoplanet_admins.county_woe_id,
                    geoplanet_admins.local_admin_woe_id
                FROM
                    geoplanet_admins
                WHERE 
                    woe_id = """ + locality + """;""")
            
            adm0_woe_id0, adm1_woe_id0, adm2_woe_id0, lau_woe_id0 = cur.fetchone()
        
        adm0_name0, adm1_name0, adm2_name0, lau_name0 = ["-1","-1","-1","-1"]
                
        if adm0_woe_id != "-1":
            cur.execute("""
                SELECT 
                    name
                FROM
                    geoplanet_places
                WHERE 
                    woe_id = """ + str(adm0_woe_id) + """;""")
            try:
                adm0_name = cur.fetchone()[0]
            except:
                pass
        
        if adm1_woe_id != "-1":
            cur.execute("""
                SELECT 
                    name
                FROM
                    geoplanet_places
                WHERE 
                    woe_id = """ + str(adm1_woe_id) + """;""")
            try:
                adm1_name = cur.fetchone()[0]
            except:
                pass
        
        if adm2_woe_id != "-1":
            cur.execute("""
                SELECT 
                    name
                FROM
                    geoplanet_places
                WHERE 
                    woe_id = """ + str(adm2_woe_id) + """;""")
            try:
                adm2_name = cur.fetchone()[0]
            except:
                pass
            
        if lau_woe_id != "-1":
            cur.execute("""
                SELECT 
                    name
                FROM
                    geoplanet_places
                WHERE 
                    woe_id = """ + str(lau_woe_id) + """;""")
            try:
                lau_name = cur.fetchone()[0]
            except:
                pass
        
        woe_name = '-1'
        
        if locality != "-1":
            cur.execute("""
                SELECT 
                    name
                FROM
                    geoplanet_places
                WHERE 
                    woe_id = """ + str(locality) + """;""")
            try:
                woe_name = cur.fetchone()[0]
            except:
                pass
        
        admins = {}
        
        admins['adm0_woe_id'] = str(adm0_woe_id)
        admins['adm1_woe_id'] = str(adm1_woe_id)
        admins['adm2_woe_id'] = str(adm2_woe_id)
        admins['lau_woe_id'] = str(lau_woe_id)
        admins['locality_woe_id'] = str(locality)
        
        admins['adm0_name'] = adm0_name
        admins['adm1_name'] = adm1_name
        admins['adm2_name'] = adm2_name
        admins['lau_name'] = lau_name
        admins['locality_name'] = woe_name
        
        #print 'admins', admins
        
        return admins

def saveTileToDatabase( self, interactivity_array ):
    for fat_pixel in interactivity_array:
        #if fat_pixel["woe_id"] == -1:
        #    continue
        
        #print 'getting admins...'
        #admins = getAdmins( fat_pixel["woe_id"] )        
        #print 'admins:', admins
                #(woe_id, name, photo_count, photo_count_total, latitude, longitude, woe_adm0, woe_adm1, woe_adm2, woe_lau, locality_lau, name_adm0, name_adm1, name_adm2, name_lau, name_locality, zoom)
        
        #print "saving...", fat_pixel
        #print "saving...", fat_pixel["photo_count"], " in ", fat_pixel["name"]
        
        curs = self.db.cursor()
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, curs)

        curs.execute("""
            INSERT 
            INTO """ + self.db_write_table_name + """
                (woe_id, name, photo_count, photo_count_total, margin, latitude, longitude, x1, y1, x2, y2, row, col, zoom)
            VALUES 
                (""" + str(fat_pixel["woe_id"]) + """,E'""" 
                     + sub("'", "\\'", fat_pixel["name"]) + """',""" 
                     + str(fat_pixel["photo_count"]) + """,""" 
                     + str(fat_pixel["photo_count_total"]) + """,""" 
                     + str(fat_pixel["margin"]) + ""","""
                     + str(fat_pixel["latitude"]) + """,""" 
                     + str(fat_pixel["longitude"]) + """,""" 
                     + fat_pixel["x1"] + """,""" 
                     + fat_pixel["y1"] + """,""" 
                     + fat_pixel["x2"] + """,""" 
                     + fat_pixel["y2"] + """,""" 
                     + fat_pixel["row"] + """,""" 
                     + fat_pixel["col"] + """,""" 
                     + str(fat_pixel["zoom"]) + """)""" )

                     #+ admins['adm0_woe_id'] + """,""" 
                     #+ admins['adm1_woe_id'] + """,""" 
                     #+ admins['adm2_woe_id'] + """,""" 
                     #+ admins['lau_woe_id'] + """,""" 
                     #+ admins['locality_woe_id'] + """,""" 
                     #+ admins['adm0_name'] + """,""" 
                     #+ admins['adm1_name'] + """,""" 
                     #+ admins['adm2_name'] + """,""" 
                     #+ admins['lau_name'] + """,""" 
                     #+ admins['locality_name'] + """,""" 

        self.db.commit()
                    
def create_utf_grid( self, interactivity_array ):
    # https://github.com/mapbox/utfgrid-spec/blob/master/1.2/utfgrid.md
    
    #3. Figure out how many unique WOEIDs you have present
    grid = []   # new "" string for each row, columns are by UTF chars; 
    keys = []   # keys in utf order as strings
    data = {}   # data that appears in the interactivity popup, key as in keys, value is arbitrary
    
    #4. Make a dictionary of attributes for those WOEIDs and populate it
    for fat_pixel in interactivity_array:
        if fat_pixel["woe_id"] == -1:
            character = ''
        else:
            character = str(fat_pixel["woe_id"])
        data[ character ] = fat_pixel["name"]
        # + "\n" + interactivity_array["name"] + "\n" + interactivity_array["photo_count"] + " of " interactivity_array["photo_count_total"] + "(" + int( float(interactivity_array["photo_count"]) / interactivity_array["photo_count_total"] * 100 ) + ") photos"
    
    for k, v in data.iteritems():
        #print k, v
        keys.append( k )
        
    #JSON doesn't allow control characters, " and \ to be encoded as their literal UTF-8 representation. 
    #Encoding an ID works as follows:
    #Add 32 to the key index. (avoiding gibberish 32 non-displaying characters at beginning of code page)
    #If the result is >= 34, add 1. (avoiding " quote character)
    #If the result is >= 92, add 1. (avoiding \ back-slash character)
    
    row_counter = 0
    row_content = ""
    
    for x in range(len(interactivity_array)):
        fat_pixel = interactivity_array[x]
        
        # find the index in the keys for this cell value
        try:
            code = keys.index( str(fat_pixel["woe_id"]) )
        except:
            code = 0

        code = code + 32
        if code >= 34: 
            code = code + 1
        if code >= 92:
            code = code + 1
        
        # are we at a new row, and not the first row?
        if x % fat_pixel_count == 0 and x > 0:
            grid.append( row_content )
            #print row_content
            row_content = ""
        else:
            row_content += unichr( code )
    
    utf_grid_result = { 'grid':grid, 'keys':keys, 'data':data } 
    
    #print "utf_grid_result: ", utf_grid_result
    
    return utf_grid_result

class Provider:
    
    def __init__(self,  layer, 
                        cell_size=8, #fatbits, yo
                        min_zoom=7, # min zoom before we start saving results
                        max_zoom=8, # or don't go any farther
                        input_field="size", 
                        woe_field="woe_id",
                        output_format="image", #or geojson, or interactivity
                        min_size=1, 
                        max_size=1000000, 
                        margin_percent=1,
                        method="size_log",
                        db_user_name="foursquare", 
                        db_read_name="foursquare",
                        db_read_table_name="flickr_locality_data",
                        db_write_name="",   #not used
                        db_write_table_name="", #not used
                        num_processes=1,
                        woe_method = "woe"
                        
                ):
        """
        """
        self.layer = layer
        self.cell_size = cell_size
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.min_size = min_size
        self.max_size = max_size
        self.margin_percent = margin_percent
        self.method = method 
        self.input_field = input_field
        self.woe_field = woe_field
        self.output_format = output_format
        self.woe_method = woe_method
        
        self.db_user_name = db_user_name
        self.db_read_name = db_read_name
        self.db_read_table_name = db_read_table_name
        self.db_write_name =db_write_name
        self.db_write_table_name = db_write_table_name
        self.num_processes = num_processes
        
        if len(self.db_write_name) > 0 and len(self.db_write_table_name) > 0:
            self.db_export = True
        
        self.log_base = (max_size - min_size) ** (1./len(colors))

        #print "db_user_name:", self.db_user_name, " db_read_name: ", self.db_read_name
        
        # Connect to the database        
        self.db = connect(user=self.db_user_name, database=self.db_read_name)
        self.cur = self.db.cursor()
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, self.cur)
        
    def renderTile(self, width, height, srs, coord):
        """
        """
        img = Image.new('RGB', (width, height), colors[0])
        draw = ImageDraw(img)
        
        interactivity_array = []
        
        base_zoom = coord.zoom
        base_row = coord.row
        base_column = coord.column
        
        #We're showing detail for three zooms in from here, as fat pixels (32 pix)
        #256 pixels / tile = 8 pixels / tile = 32 pixels (which is 2^5)

        tile_pixel_width = 256
        #print 'coord:', coord
        #print 'base_zoom:', base_zoom
        
        # 256 pixel tile == 2^8 pixel tile, so this is a constant
        tile_power_of_two = 8
        
        # we want 8x8 fatbits == 2^3 pixel fatbits
        #TODO: use self.cell_size to find log of 2 to x?
        pixel_power_of_two = int(log( self.cell_size, 2 ))
        
        fat_pixel_width = 2**pixel_power_of_two
        self.fat_pixel_count = 2**(tile_power_of_two - pixel_power_of_two)

        # adjust the coord to be the pixel zoom
        coord = coord.zoomBy(tile_power_of_two - pixel_power_of_two)
        
        #print "fat_pixel_count: ", fat_pixel_count
        #print "coord: ", coord       
        #print 'over_sample_zoom_tile_width: ', over_sample_zoom_tile_width
        
        #find the fat_pixel with the maximum photo count
        max_count = 0
        top_count = 0
        top_margin = 0
        
        #We should be seeing 64 cells (8x8) output image
        for row in range( self.fat_pixel_count ):
            for col in range( self.fat_pixel_count ):
                
                ul = coord.right(col).down(row)
                lr = ul.right().down()
                
                #Calculate key for the size dict
                subquad = Coordinate(ul.row, ul.column, ul.zoom)
                
                #print 'subquad:', subquad
                
                # these values should always be within (0, 256)
                x1 = col * fat_pixel_width
                x2 = (col + 1) * fat_pixel_width
                y1 = row * fat_pixel_width
                y2 = (row + 1) * fat_pixel_width
                
                #Draw fat pixel based on the returned color based on count (size) in that subquad in the dictionary
                #Implied that no-data is color[0], above where the img is instantiated
                
                enumeration = count_votes( self, subquad )
                                
                if max_count < enumeration["photo_count_total"]:
                    max_count = enumeration["photo_count_total"]
                
                if top_count < enumeration["photo_count0"]:
                    top_count = enumeration["photo_count0"]
                    
                if self.output_format == "utf_grid":
                    nw = osm.coordinateLocation(subquad)
                    se = osm.coordinateLocation(subquad.right().down())

                    lat = (nw.lat - se.lat) / 2 + se.lat
                    lon = (se.lon - nw.lon) / 2 + nw.lon
                                        
                    interactivity_array.append( {   "photo_count_total":enumeration["photo_count_total"], 
                                                    "woe_id":enumeration["woe_id0"], 
                                                    #"woe_id_lau":enumeration["woe_id0_lau"], 
                                                    #"woe_id_adm2":enumeration["woe_id0_adm2"], 
                                                    #"woe_id_adm1":enumeration["woe_id0_adm1"], 
                                                    "woe_id_adm0":enumeration["woe_id0_adm0"],
                                                    "name":enumeration["name0"], 
                                                    "photo_count":enumeration["photo_count0"],
                                                    "margin":enumeration["margin0"],
                                                    "latitude":lat,
                                                    "longitude":lon, 
                                                    "x1": str(nw.lon),
                                                    "y1": str(se.lat),
                                                    "x2": str(se.lon),
                                                    "y2": str(nw.lat),
                                                    "row":str(base_row + row),
                                                    "col":str(base_column + col),
                                                    "zoom": coord.zoom } )
                elif self.method == "size_log":
                    draw.rectangle((x1, y1, x2, y2), size_color_log(int( enumeration[self.input_field]) ))
                elif self.method == "size":
                    draw.rectangle((x1, y1, x2, y2), size_color(int( enumeration[self.input_field]) ))
                elif self.method == "unique_id":
                    draw.rectangle((x1, y1, x2, y2), size_color_unique_id(int( enumeration[self.input_field]) )) 

        if self.output_format == "utf_grid":
            #print "interactivity_array: ", interactivity_array
            #grid_utf = create_utf_grid( self, interactivity_array )
            grid_utf = { 'grid':['','.'] }
                
            if max_count == 0:
                raise NothingToSeeHere()
            
            is_saveable = False
            
            # Are we at the last requested zoom?
            if coord.zoom == self.max_zoom:
                is_saveable = True
            # Are we at the minimum viable zoom but with little to no data?
            if (coord.zoom >= self.min_zoom) and (max_count <= self.min_size):
                is_saveable = True
            # Are we viable zoom, viable count, and no ambiguity as to the 100% within margin the winner?
            if (coord.zoom >= (self.min_zoom + 2)) and (max_count > self.max_size) and ((top_count >= (max_count * self.margin_percent)) or ((max_count - top_count) < self.min_size)):
                is_saveable = True
            # Don't want to dig for needles
            #if coord.zoom == 17 and base_row == 50816 and base_column == 21045:
            #    print '(coord.zoom >= (self.min_zoom + 1)) and ((max_count - top_count) < self.min_size):'
            #    print coord.zoom,(self.min_zoom + 1),max_count, top_count, self.min_size
            if (coord.zoom >= (self.min_zoom + 1)) and ((max_count - top_count) < self.min_size):
            #(max_count > self.min_size) and 
                is_saveable = True

            # and (interactivity_array["margin"] >= self.margin_percent)

            if is_saveable:
                #print "should save to DB"
                #print "interactivity_array: ", interactivity_array                
                saveTileToDatabase( self, interactivity_array )
                raise NothingMoreToSeeHere( SaveableResponse(json.dumps(grid_utf)) )
            else:            
                return SaveableResponse(json.dumps(grid_utf))
                
        elif self.output_format == "geojson":
            grid_utf = create_utf_grid( self, interactivity_array )
            return SaveableResponse(json.dumps(grid_utf))
        else:
            return img
            
    def getTypeByExtension(self, extension):
        """ Get mime-type and format by file extension.

            This only accepts png (image), json (utf_grid interactivity), or geojson (vector)".
        """
        
        if self.output_format == "utf_grid":        
            if extension.lower() != 'json':
                raise KnownUnknown('FourSquare provider only makes .json tiles, not "%s"' % extension)

        if extension.lower() == 'json':
            return 'text/json', 'JSON'

        if extension.lower() == 'geojson':
            return 'text/json', 'GeoJSON'
        
        if extension.lower() == 'png':
            return 'image/png', 'PNG'
    
        raise KnownUnknown('FourSquare Provider only makes .geojson, .json, and .png tiles, not "%s"' % extension)

class SaveableResponse:
    """ Wrapper class for JSON response that makes it behave like a PIL.Image object.

        TileStache.getTile() expects to be able to save one of these to a buffer.
    """
    def __init__(self, content):
        self.content = content

    def save(self, out, format):
        #
        # Serialize
        #
        if format in ('GeoJSON'):
            #print "GeoJSON: ", self.content
            content = self.content
            
            #if 'wkt' in content['crs']:
            #    content['crs'] = {'type': 'link', 'properties': {'href': '0.wkt', 'type': 'ogcwkt'}}
            #else:
            #    del content['crs']

        elif format in ('PNG'):
            content = self.content
        
        else:
            raise KnownUnknown('FourSquare response only saves .png, .json, and .geojson tiles, not "%s"' % format)

        #
        # Encode
        #
        if format in ('GeoJSON'):
            #indent = self.verbose and 2 or None
            indent = 2
            
            encoded = JSONEncoder(indent=indent).iterencode(content)
            out.write(encoded)

        elif format in ('JSON'):
            out.write(content)

        elif format in ('PNG'):
            out.write(content)
    
if __name__ == '__main__':
    p = Provider(None)
            
    #This is done in an odd order where the Zoom is last
    p.renderTile(256, 256, '', Coordinate(3, 2, 3)).save('out.png')