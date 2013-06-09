SOURCE

Scraped ~10 gb of Flickr geocoded photos as CSVs using the scripts in betashapes. Augmented with foursquare checkin data.

CLEAN-UP

For each admin-0, admin-1, admin-2, locality, and neighborhood, we need to add in that per CSV on DB import.

IMPORTING TO DATABAS
Loading CSV into PostGIS

DB setup:

createuser foursquare
#Shall the new role be a superuser? (y/n) y

#Make sure we're on the SSD drive
#http://www.postgresql.org/docs/8.1/static/sql-createtablespace.html
#Ensure the `postgres` folder is owned by the `postgres` OS user.

CREATE TABLESPACE geo_ssd LOCATION '/Volumes/Geo/postgres';

#http://postgis.refractions.net/documentation/manual-2.0/postgis_installation.html#create_new_db_extensions

createdb -U postgres -O foursquare --tablespace geo_ssd foursquare
psql -d foursquare -c "CREATE EXTENSION postgis;"


#createdb -U postgres -O foursquare -T template_postgis foursquare --tablespace osm
#note --tablespace osm is on a separate SSD drive than the main tablespace.
#make sure the 2 spatial tables are owned by foursquare user.


Table import:

Optional: Rename flickr_adm0_data to flickr_adm0_data_old

    ALTER TABLE flickr_adm0_data RENAME TO flickr_adm0_data_old;

Now we will create the new table flickr_data.

# http://www.postgresql.org/docs/8.2/static/sql-copy.html
# http://www.postgresql.org/docs/9.2/interactive/datatype-numeric.html
# implied header on each file:
# photo_id	woe_id	longitude	latitude
# 6981212365	2514294	-122.369155	48.166085

	#get into postgres
	psql -U foursquare
    DROP TABLE flickr_adm0_data;
    CREATE TABLE flickr_adm0_data(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);	
    \copy flickr_adm0_data from '/Volumes/Data/Downloads/simplegeo-betashapes-8f7fff0/data_world_admin0/photos.txt'
    

Create point geoms:

#create a bonifide geometry column instead of loose geom in two columns
#http://postgis.org/docs/AddGeometryColumn.html
SELECT AddGeometryColumn('flickr_adm0_data', 'photo_geom', 4326, 'POINT', 2, true);

#Populate that new field with POINT, in geographic projection
UPDATE flickr_adm0_data SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);

#Make it fast
#http://postgis.refractions.net/documentation/manual-1.5/ch04.html#id2670643
CREATE INDEX photo_index ON flickr_adm0_data USING GIST ( photo_geom );


Calculate the heatmap data:

python measure_sizes.py -u foursquare -d foursquare -t flickr_adm2_data -s 0/0/0 -o flickr_adm2_heatmap.csv


Draw heatmaps:

./tilestache-seed.py -c tilestache.cfg -l size -b 84 -180 -84 180 --to-mbtiles flickr_adm0_density.mbtiles 0 1 2 3 4 5 6 7

./tilestache-seed.py -c tilestache.cfg -l flickr_locality_density -b 37.932 -122.590 37.652 -122.088 --to-mbtiles flickr_locality_density_20130106a.mbtiles 7

#indonesia
./tilestache-seed.py -c tilestache.cfg -l flickr_locality_density -b 7.8 92.3 -13.0 144.0 --to-mbtiles flickr_locality_density_20130106b_indonesia.mbtiles 6 7 8 9 10 11 12 13 14 15

./tilestache-seed.py -x -q -c tilestache.cfg -l checkins --recon -b -5.842 105.876 -6.058 106.147 -e json 12 13 14 15 16 17 18

# How many are in that area of interest?

SELECT COUNT(latitude) FROM checkins WHERE photo_geom && ST_SetSRID(ST_MakeBox2D(ST_MakePoint((105.876), (-6.058)), ST_MakePoint((106.147), (-5.842))), 4326);


# What connections are active with Postgres?
select * from pg_stat_activity;

# status report
select sum(photo_count_total), count(zoom), max(zoom) from quatroshapes;

# Starting and stopping Postgres
http://www.sd-kyber.com/library/onlineNotes/psqlOSX.html
pg_stop
pg_start

#Table for storing quatroshape voting into:

CREATE TABLE quatroshapes (latitude float, longitude float, x1 float, y1 float, x2 float, y2 float, zoom int, row int, col int, photo_count_total integer, woe_id integer, name varchar(250), photo_count integer, margin float, woe_adm0 integer, woe_adm1 integer, woe_adm2 integer, woe_lau integer, locality_lau integer, name_adm0 varchar(250), name_adm1 varchar(250), name_adm2 varchar(250), name_lau varchar(250), name_locality varchar(250));

SELECT AddGeometryColumn('quatroshapes', 'the_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('quatroshapes', 'poly_geom', 4326, 'POLYGON', 2, true);

CREATE INDEX quatro_index ON quatroshapes USING GIST ( the_geom );

UPDATE quatroshapes SET the_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE quatroshapes SET poly_geom = ST_SetSRID(ST_MakeEnvelope(x1, y1, x2, y2),4326);

pgsql2shp -f shp/humboldt_merged.shp -g poly_geom -u foursquare foursquare quatroshapes

ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 -overwrite shp/jakarta_1000.shp -nlt POLYGON PG:"host=localhost user=foursquare dbname=foursquare" -sql "SELECT name, woe_id, margin, photo_count_total, zoom, row, col, poly_geom FROM quatroshapes"


# utf-8 shps
# REMEMBER to make a .cpg file with UTF-8 as the sole text contents.
# the *.cpg file should be named same as the *.shp part.

Stached 3214 tiles in 3:21:37.738275 (16.0 tpm)
Stached 3214 tiles in 0:23:14.385987 (139.0 tpm)

./tilestache-seed.py -x -c tilestache.cfg -l flickr_locality_interactivity --recon -b 41.113 -124.423 40.496 -123.865 -e json 9 10 11 12 13 14 15 16 17 18

####

http://developer.yahoo.com/geo/geoplanet/guide/concepts.html

PLACE TYPES

Places are categorized to help identify the place. These Place Types have unique codes that may be used to filter results for some resources. They also have localized names, so they can be displayed along with the localized place name. The following table lists the supported place types.
Place Type Name	Place Type Code	Description
Continent	29	One of the major land masses on the earth. GeoPlanet is built on a seven-continent model: Asia (24865671), Africa (24865670), North America (24865672), South America (24865673), Antarctica (28289421), Europe (24865675), and Pacific (Australia, New Zealand, and the other islands in the Pacific Ocean -- 24865674).
Country	12	One of the countries and dependent territories defined by the ISO 3166-1 standard.
Admin	8	One of the primary administrative areas within a country. Place type names associated with this place type include: State, Province, Prefecture, Country, Region, Federal District.
Admin2	9	One of the secondary administrative areas within a country. Place type names associated with this place type include: County, Province, Parish, Department, District.
Admin3	10	One of the tertiary administrative areas within a country. Place type names associated with this place type include: Commune, Municipality, District, Ward.
Town	7	One of the major populated places within a country. This category includes incorporated cities and towns, major unincorporated towns and villages.
Suburb	22	One of the subdivisions within a town. This category includes suburbs, neighborhoods, wards.
Postal Code	11	One of the postal code areas within a country. This category includes both full postal codes (such as those in UK and CA) and partial postal codes. Examples include: SW1A 0AA (UK), 90210 (US), 179-0074 (JP).
Supername	19	A place that refers to a region consisting of multiple countries or an historical country that has been dissolved into current countries. Examples include Scandinavia, Latin America, USSR, Yugoslavia, Western Europe, and Central America.
Colloquial	24	Examples are New England, French Riviera, 関西地方(Kansai Region), South East England, Pacific States, and Chubu Region.
Time Zone	31	A place that refers to an area defined by the Olson standard. Examples include America/Los Angeles, Asia/Tokyo, Europe/Madrid.



###
For the tables that have raw photo data from Flickr
###


CREATE TABLE flickr_adm0_data(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);	
CREATE TABLE flickr_adm1_data(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);
CREATE TABLE flickr_adm2_data(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);
CREATE TABLE flickr_locality_data(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);
CREATE TABLE flickr_neighborhood_data(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);	

\copy flickr_adm0_data from '/Volumes/Data/quattroshapes/data_world_admin0/photos.txt'
\copy flickr_adm1_data from '/Volumes/Data/quattroshapes/data_world_admin1/photos.txt'
\copy flickr_adm2_data from '/Volumes/Data/quattroshapes/data_world_admin2/photos.txt'
\copy flickr_locality_data from '/Volumes/Data/quattroshapes/data_world_localities/photos.txt'
\copy flickr_neighborhood_data from '/Volumes/Data/quattroshapes/data_world_neighborhoods/photos.txt'

SELECT AddGeometryColumn('flickr_adm0_data', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_adm1_data', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_adm2_data', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_locality_data', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_neighborhood_data', 'photo_geom', 4326, 'POINT', 2, true);

UPDATE flickr_adm0_data SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_adm1_data SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_adm2_data SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_locality_data SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_neighborhood_data SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);

CREATE INDEX photo_adm0_index ON flickr_adm0_data USING GIST ( photo_geom );
CREATE INDEX photo_adm1_index ON flickr_adm1_data USING GIST ( photo_geom );
CREATE INDEX photo_adm2_index ON flickr_adm2_data USING GIST ( photo_geom );
CREATE INDEX photo_locality_index ON flickr_locality_data USING GIST ( photo_geom );
CREATE INDEX photo_neighborhood_index ON flickr_neighborhood_data USING GIST ( photo_geom );

CREATE INDEX woe_adm0_index ON flickr_adm0_data ( woe_id );
CREATE INDEX woe_adm1_index ON flickr_adm1_data ( woe_id );
CREATE INDEX woe_adm2_index ON flickr_adm2_data ( woe_id );
CREATE INDEX woe_locality_index ON flickr_locality_data ( woe_id );
CREATE INDEX woe_neighborhood_index ON flickr_neighborhood_data ( woe_id );


###
For the tables that don't have outliers
###

CREATE TABLE flickr_adm0_data_clean(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);	
CREATE TABLE flickr_adm1_data_clean(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);
CREATE TABLE flickr_adm2_data_clean(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);
CREATE TABLE flickr_locality_data_clean(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);
CREATE TABLE flickr_neighborhood_data_clean(photo_id bigint, woe_id bigint, longitude double precision, latitude double precision);	

SELECT AddGeometryColumn('flickr_adm0_data_clean', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_adm1_data_clean', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_adm2_data_clean', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_locality_data_clean', 'photo_geom', 4326, 'POINT', 2, true);
SELECT AddGeometryColumn('flickr_neighborhood_data_clean', 'photo_geom', 4326, 'POINT', 2, true);

UPDATE flickr_adm0_data_clean SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_adm1_data_clean SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_adm2_data_clean SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_locality_data_clean SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);
UPDATE flickr_neighborhood_data_clean SET photo_geom = ST_SetSRID(ST_MakePoint(longitude, latitude),4326);


CREATE INDEX photo_adm0_clean_index ON flickr_adm0_data_clean USING GIST ( photo_geom );
CREATE INDEX photo_adm1_clean_index ON flickr_adm1_data_clean USING GIST ( photo_geom );
CREATE INDEX photo_adm2_clean_index ON flickr_adm2_data_clean USING GIST ( photo_geom );
CREATE INDEX photo_locality_clean_index ON flickr_locality_data_clean USING GIST ( photo_geom );
CREATE INDEX photo_neighborhood_clean_index ON flickr_neighborhood_data_clean USING GIST ( photo_geom );

CREATE INDEX woe_adm0_clean_index ON flickr_adm0_data_clean ( woe_id );
CREATE INDEX woe_adm1_clean_index ON flickr_adm1_data_clean ( woe_id );
CREATE INDEX woe_adm2_clean_index ON flickr_adm2_data_clean ( woe_id );
CREATE INDEX woe_locality_clean_index ON flickr_locality_data_clean ( woe_id );
CREATE INDEX woe_neighborhood_clean_index ON flickr_neighborhood_data_clean ( woe_id );

CREATE INDEX place_woe_id_index ON geoplanet_adjacencies ( place_woe_id );
CREATE INDEX placetype_index ON geoplanet_places ( placetype );
