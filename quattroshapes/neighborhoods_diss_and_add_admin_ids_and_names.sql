-- 1. First the points for the voronoi
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quatroshapes_neighborhoods_pts.shp \
	-nlt POLYGON PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT woe_id, name, the_geom FROM quatroshapes_neighborhoods"


-- 2. Then the core quattroshapes part

-- do the dissolve union
CREATE TABLE quatroshapes_neighborhoods_diss AS
SELECT woe_id, count(woe_id) as quad_count, sum(photo_count) as photo_sum, max(photo_count) as photo_max,
	   ST_Union(f.poly_geom) as singlegeom
	 FROM quatroshapes_neighborhoods As f
GROUP BY woe_id;

-- Update the geometry_columns table
SELECT Populate_Geometry_Columns();



-- Then add the attrs back

-- Add the columns
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN geoname_id numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_adm0 numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_adm1 numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_adm2 numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_lau numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_locality numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name_en character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name_adm0 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name_adm1 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name_adm2 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name_lau character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN name_locality character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_version character varying(10);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN placetype character varying(50);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN woe_funk character varying(50);

-- set the default
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_version = 'unknown';

-- Populate the columns, from GeoPlanet 7.10.0
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	name = geoplanet_places.name,
	name_en = geoplanet_places.english_name,
	geoname_id = geoplanet_places.gn_id,
	woe_adm0 = geoplanet_places.woe_adm0,
	woe_adm1 = geoplanet_places.woe_adm1,
	woe_adm2 = geoplanet_places.woe_adm2,
	woe_lau = geoplanet_places.woe_lau,
	woe_locality = geoplanet_places.woe_locality,
	name_adm0 = geoplanet_places.name_adm0,
	name_adm1 = geoplanet_places.name_adm1,
	name_adm2 = geoplanet_places.name_adm2,
	name_lau = geoplanet_places.name_lau,
	name_locality = geoplanet_places.name_locality,
	placetype = geoplanet_places.placetype,
	woe_funk = geoplanet_places.woe_funk,
	woe_version = '7.10.0'
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss.woe_id = geoplanet_places.woe_id;

-- make sure the locality is right on the one's 
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_locality = geoplanet_places.woe_locality,
	name_locality = geoplanet_places.name_locality
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss.woe_locality = geoplanet_places.woe_id AND
	quatroshapes_neighborhoods_diss.woe_funk = 'Parented by a neighborhood' AND
	geoplanet_places.placetype = 'Town';

-- we changed a bunch of other ones
-- make sure the locality is right on the one's 
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_locality = geoplanet_places.woe_locality,
	name_locality = geoplanet_places.name_locality
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss.woe_id = geoplanet_places.woe_id
	--AND quatroshapes_neighborhoods_diss.woe_lau = quatroshapes_neighborhoods_diss.woe_locality
	;


-- SPECIAL CASES

-- Laguna Heights, San Francisco, CA
UPDATE geoplanet_places SET	woe_locality = 2487956, name_locality = 'San Francisco' WHERE woe_id = 2434643; 

-- Le Frak City, New York, NY
UPDATE geoplanet_places SET woe_locality = 2459115, name_locality = 'New York' WHERE woe_id = 23511863; 


UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_locality = geoplanet_places.woe_locality,
	name_locality = geoplanet_places.name_locality
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss.woe_id IN (23511863, 2434643) AND
	quatroshapes_neighborhoods_diss.woe_locality = geoplanet_places.woe_id;

-- post lau=locality fix
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_locality = geoplanet_places.woe_locality,
	name_locality = geoplanet_places.name_locality
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss.woe_id = geoplanet_places.woe_id;



-- General case
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_locality = geoplanet_places.woe_locality,
	name_locality = geoplanet_places.name_locality
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss.woe_locality = geoplanet_places.woe_id;


WITH 
	parentlocality_woe AS 
		( SELECT name, woe_id, placetype FROM geoplanet_places )
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	woe_locality = geoplanet_places.woe_locality,
	name_locality = geoplanet_places.name_locality
FROM
	geoplanet_places, parentlocality_woe
WHERE
	quatroshapes_neighborhoods_diss.woe_id = geoplanet_places.woe_id AND
	geoplanet_places.woe_locality = parentlocality_woe.woe_id AND
	quatroshapes_neighborhoods_diss.woe_funk = 'Parented by a neighborhood' AND
	quatroshapes_neighborhoods_diss.woe_version = '7.10.0' AND
	parentlocality_woe.placetype = 'Town';


-- some localadmin don't have localites and the suburbs are parented directly.
-- while that makes sense administratively, it's poor in terms of map display

UPDATE 
	quatroshapes_neighborhoods_diss
SET
	woe_locality = woe_lau,
	name_locality = name_lau
WHERE 
	quatroshapes_neighborhoods_diss.woe_locality IS NULL;



-- add the GN versions of the same
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN gn_name character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN gn_fcode character varying(10);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN gn_adm0_cc character varying(2);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN gn_name_adm1 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN gn_locality numeric;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN gn_name_locality character varying(200);


UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	gn_name = geoname.name,
	gn_fcode = geoname.fcode,
	gn_adm0_cc = geoname.cc2,
	gn_name_adm1 = geoname.admin1
FROM
	geoname
WHERE
	quatroshapes_neighborhoods_diss.geoname_id = geoname.geonameid;


WITH 
	parentlocality_woe AS 
		( SELECT name, woe_id, gn_id, gn_name FROM geoplanet_places )
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	gn_locality = parentlocality_woe.gn_id,
	gn_name_locality = parentlocality_woe.gn_name
FROM
	parentlocality_woe
WHERE
	quatroshapes_neighborhoods_diss.woe_locality = parentlocality_woe.woe_id;

-- fill in more cc
WITH 
	parentlocality_woe AS 
		( SELECT name, woe_id, gn_id, gn_name FROM geoplanet_places ),
	parentlocality_gn AS 
		( SELECT name, geonameid, country FROM geoname )
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	gn_adm0_cc = parentlocality_gn.country
FROM
	parentlocality_woe, parentlocality_gn
WHERE
	quatroshapes_neighborhoods_diss.woe_locality = parentlocality_woe.woe_id AND
	parentlocality_woe.gn_id = parentlocality_gn.geonameid AND
	quatroshapes_neighborhoods_diss.gn_adm0_cc IS NULL;

-- fill in more admin1
WITH 
	parentlocality_woe AS 
		( SELECT name, woe_id, gn_id, gn_name FROM geoplanet_places ),
	parentlocality_gn AS 
		( SELECT name, geonameid, admin1 FROM geoname )
UPDATE 
	quatroshapes_neighborhoods_diss
SET	
	gn_name_adm1 = parentlocality_gn.admin1
FROM
	parentlocality_woe, parentlocality_gn
WHERE
	quatroshapes_neighborhoods_diss.woe_locality = parentlocality_woe.woe_id AND
	parentlocality_woe.gn_id = parentlocality_gn.geonameid AND
	quatroshapes_neighborhoods_diss.gn_name_adm1 IS NULL AND
	quatroshapes_neighborhoods_diss.woe_locality = quatroshapes_neighborhoods_diss.woe_lau;


-- how many are missing from GeoPlanet 7.10
SELECT 
	count(*)
FROM
	quatroshapes_neighborhoods_diss
LEFT OUTER JOIN 
	geoplanet_places
ON 
	geoplanet_places.woe_id = quatroshapes_neighborhoods_diss.woe_id
WHERE 
	geoplanet_places.woe_id IS null;
	
-- let's set those from GeoPlanet 7.3.1 instead
WITH missing AS (
	SELECT 
		quatroshapes_neighborhoods_diss.woe_id
	FROM
		quatroshapes_neighborhoods_diss
	LEFT OUTER JOIN 
		geoplanet_places
	ON 
		geoplanet_places.woe_id = quatroshapes_neighborhoods_diss.woe_id
	WHERE 
		geoplanet_places.woe_id IS null
)
UPDATE 
	quatroshapes_neighborhoods_diss
SET
	name = geoplanet_places_7_3_1.name,
	name_en = geoplanet_places_7_3_1.name,
	woe_adm0 = geoplanet_places_7_3_1.woe_adm0,
	woe_adm1 = geoplanet_places_7_3_1.woe_adm1,
	woe_adm2 = geoplanet_places_7_3_1.woe_adm2,
	woe_lau = geoplanet_places_7_3_1.woe_lau,
	woe_locality = geoplanet_places_7_3_1.woe_locality,
	name_adm0 = geoplanet_places_7_3_1.name_adm0,
	name_adm1 = geoplanet_places_7_3_1.name_adm1,
	name_adm2 = geoplanet_places_7_3_1.name_adm2,
	name_lau = geoplanet_places_7_3_1.name_lau,
	name_locality = geoplanet_places_7_3_1.name_locality,
	placetype = geoplanet_places_7_3_1.placetype,
	woe_funk = geoplanet_places_7_3_1.woe_funk,
	woe_version = '7.3.1'
FROM
	missing, geoplanet_places_7_3_1
WHERE 
	quatroshapes_neighborhoods_diss.woe_id = missing.woe_id AND
	quatroshapes_neighborhoods_diss.woe_id = geoplanet_places_7_3_1.woe_id;
	
-- woe_id  | name | name_en 
----------+------+---------
-- 55999165 |      | 
-- 55999062 |      | 
-- 55999530 |      | 
-- 55999278 |      | 
-- 20162160 |      | 

UPDATE 
	quatroshapes_neighborhoods_diss
SET
	name = 'Limehouse',
	name_en = 'Limehouse',
	woe_adm0 = 23424775,
	woe_adm1 = 2344922,
	woe_adm2 = 29375078,
	woe_lau = NULL,
	woe_locality = 4348,
	name_adm0 = 'Canada',
	name_adm1 = 'Ontario',
	name_adm2 = 'Halton',
	name_lau = '',
	name_locality = 'Acton'
WHERE 
	quatroshapes_neighborhoods_diss.woe_id = 55999165;

UPDATE 
	quatroshapes_neighborhoods_diss
SET
	name = 'Belfountain',
	name_en = 'Belfountain',
	woe_adm0 = 23424775,
	woe_adm1 = 2344922,
	woe_adm2 = 29375178,
	woe_lau = NULL,
	woe_locality = 23396905,
	name_adm0 = 'Canada',
	name_adm1 = 'Ontario',
	name_adm2 = 'Peel',
	name_lau = '',
	name_locality = 'Caledon'
WHERE 
	quatroshapes_neighborhoods_diss.woe_id = 55999062;

UPDATE 
	quatroshapes_neighborhoods_diss
SET
	name = 'Inglewood',
	name_en = 'Inglewood',
	woe_adm0 = 23424775,
	woe_adm1 = 2344922,
	woe_adm2 = 29375178,
	woe_lau = NULL,
	woe_locality = 23396905,
	name_adm0 = 'Canada',
	name_adm1 = 'Ontario',
	name_adm2 = 'Peel',
	name_lau = '',
	name_locality = 'Caledon'
WHERE 
	quatroshapes_neighborhoods_diss.woe_id = 55999530;

UPDATE 
	quatroshapes_neighborhoods_diss
SET
	name = 'Claremont',
	name_en = 'Claremont',
	woe_adm0 = 23424775,
	woe_adm1 = 2344922,
	woe_adm2 = 29375180,
	woe_lau = NULL,
	woe_locality = 4364,
	name_adm0 = 'Canada',
	name_adm1 = 'Ontario',
	name_adm2 = 'Durham',
	name_lau = '',
	name_locality = 'Pickering'
WHERE 
	quatroshapes_neighborhoods_diss.woe_id = 55999278;

UPDATE 
	quatroshapes_neighborhoods_diss
SET
	name = 'Gemeinde Mühltal',
	name_en = 'Gemeinde Muhltal',
	woe_adm0 = 23424829,
	woe_adm1 = 2345485,
	woe_adm2 = 12596968,
	woe_lau = NULL,
	woe_locality = NULL,
	name_adm0 = 'Germany',
	name_adm1 = 'Hesse',
	name_adm2 = 'Darmstadt-Dieburg',
	name_lau = '',
	name_locality = ''
WHERE 
	quatroshapes_neighborhoods_diss.woe_id = 20162160;



ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN hoods int;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN local_sum int;
ALTER TABLE quatroshapes_neighborhoods_diss ADD COLUMN local_max int;

WITH 
	locality_hoods AS 
		( SELECT woe_locality, count(*) as neighbhoods, sum(photo_sum) as local_sum, max(photo_sum) as local_max FROM quatroshapes_neighborhoods_diss GROUP BY woe_locality )
UPDATE 
	quatroshapes_neighborhoods_diss
SET
	hoods = locality_hoods.neighbhoods,
	local_sum = locality_hoods.local_sum,
	local_max = locality_hoods.local_max
FROM
	locality_hoods
WHERE
	quatroshapes_neighborhoods_diss.woe_locality = locality_hoods.woe_locality;


-- now back in the shell, let's export
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quatroshapes_neighborhoods_diss.shp -nlt POLYGON \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT woe_id, name, name_en, name_adm0, name_adm1, name_adm2, name_lau, name_locality as  name_local, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_locality as woe_local, woe_version as woe_ver, placetype, geoname_id as gn_id, gn_name, gn_fcode, gn_adm0_cc, gn_name_adm1 as gn_namadm1, gn_locality as gn_local, gn_name_locality as gn_nam_loc, woe_funk, quad_count, photo_sum, photo_max, hoods as localhoods, local_sum, local_max, singlegeom FROM quatroshapes_neighborhoods_diss"


-- 3. Then the buffer quattroshapes part (to clip the voronoi)

-- do the dissolve union
CREATE TABLE quatroshapes_neighborhoods_buffer_diss AS
(SELECT 1,
	   ST_Union(f.buffer_geom) as singlegeom
	 FROM quatroshapes_neighborhoods As f);

-- Update the geometry_columns table
SELECT Populate_Geometry_Columns();

-- there is only 1 shape, so no attr to join

-- now back in the shell, let's export
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quatroshapes_neighborhoods_buffer_diss.shp \
	-nlt POLYGON PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT * FROM quatroshapes_neighborhoods_buffer_diss"

	



-- locality dissolve version (for attr only)

-- do the dissolve union
DROP TABLE quatroshapes_neighborhoods_diss_as_locality;

CREATE TABLE quatroshapes_neighborhoods_diss_as_locality AS
SELECT woe_locality as woe_id, count(*) as localhoods, sum(photo_sum) as local_sum, max(photo_sum) as local_max,
	   ST_Union(f.singlegeom) as singlegeom
	 FROM quatroshapes_neighborhoods_diss As f
GROUP BY woe_locality;

-- Update the geometry_columns table
SELECT Populate_Geometry_Columns();


-- Add the columns
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN geoname_id numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_adm0 numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_adm1 numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_adm2 numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_lau numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_locality numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name_en character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name_adm0 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name_adm1 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name_adm2 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name_lau character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN name_locality character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_version character varying(10);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN placetype character varying(50);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN woe_funk character varying(50);

-- set the default
UPDATE 
	quatroshapes_neighborhoods_diss_as_locality
SET	
	woe_version = 'unknown';

-- Populate the columns, from GeoPlanet 7.10.0
UPDATE 
	quatroshapes_neighborhoods_diss_as_locality
SET	
	name = geoplanet_places.name,
	name_en = geoplanet_places.english_name,
	geoname_id = geoplanet_places.gn_id,
	woe_adm0 = geoplanet_places.woe_adm0,
	woe_adm1 = geoplanet_places.woe_adm1,
	woe_adm2 = geoplanet_places.woe_adm2,
	woe_lau = geoplanet_places.woe_lau,
	woe_locality = geoplanet_places.woe_locality,
	name_adm0 = geoplanet_places.name_adm0,
	name_adm1 = geoplanet_places.name_adm1,
	name_adm2 = geoplanet_places.name_adm2,
	name_lau = geoplanet_places.name_lau,
	name_locality = geoplanet_places.name_locality,
	placetype = geoplanet_places.placetype,
	woe_funk = geoplanet_places.woe_funk,
	woe_version = '7.10.0'
FROM
	geoplanet_places
WHERE
	quatroshapes_neighborhoods_diss_as_locality.woe_id = geoplanet_places.woe_id;
	

-- add the GN versions of the same
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN gn_name character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN gn_fcode character varying(10);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN gn_adm0_cc character varying(2);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN gn_name_adm1 character varying(200);
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN gn_locality numeric;
ALTER TABLE quatroshapes_neighborhoods_diss_as_locality ADD COLUMN gn_name_locality character varying(200);

UPDATE 
	quatroshapes_neighborhoods_diss_as_locality
SET	
	gn_name = geoname.name,
	gn_fcode = geoname.fcode,
	gn_adm0_cc = geoname.country,
	gn_name_adm1 = geoname.admin1,
	gn_locality = geoname.geonameid,
	gn_name_locality = geoname.name
FROM
	geoname
WHERE
	quatroshapes_neighborhoods_diss_as_locality.geoname_id = geoname.geonameid;
	
-- now back in the shell, let's export
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quatroshapes_neighborhoods_diss_as_locality.shp -nlt POLYGON \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT woe_id, name, name_en, name_adm0, name_adm1, name_adm2, name_lau, name_locality as  name_local, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_locality as woe_local, woe_version as woe_ver, placetype, geoname_id as gn_id, gn_name, gn_fcode, gn_adm0_cc, gn_name_adm1 as gn_namadm1, gn_locality as gn_local, gn_name_locality as gn_nam_loc, woe_funk, localhoods, local_sum, local_max, singlegeom FROM quatroshapes_neighborhoods_diss_as_locality"

