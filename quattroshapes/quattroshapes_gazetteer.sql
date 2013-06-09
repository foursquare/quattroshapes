--http://www.codinghorror.com/blog/2007/10/a-visual-explanation-of-sql-joins.html

DROP TABLE quattroshapes_gazetteer;

CREATE TABLE quattroshapes_gazetteer AS
(WITH
	gn_with_woe AS
	(	SELECT 
			geonameid as gn_id, woe_id, name, country, photos as checkins, population, asciiname, admin1, admin2, fclass, fcode, the_geom
		FROM 
			geoname
		WHERE 
			population > 0 OR
			fclass = 'A' OR
			fcode IN ('PPLG','PPLC','PPLCH','PPLA','PPLA2','PPLA3','PPLA4') OR 
			woe_id IS NOT NULL
 	),
	woe_with_gn AS
	(	SELECT 
			woe_id, gn_id, name, english_name, placetype, iso, language, parent_id, woe_locality, woe_lau, woe_adm2, woe_adm1, woe_adm0, name_locality, name_lau, name_adm2, name_adm1, name_adm0, gns_id, accuracy, gn_matcht, spatial_ac, woe_funk, photos_again, photos_again_aggregate, photos_children_places, geom
		FROM 
			geoplanet_places
		WHERE 
			photos > 0 OR
			placetype IN ('Country','State','County','LocalAdmin') OR 
			gn_id IS NOT NULL OR
			accuracy IN ('flickr aggregate Suburb','flickr aggregate Town','flickr median', 'flickr children Town','geonames match great','geonames match','geonames match round 2','other match great')
 	)
SELECT
-- 	count(*)
 	--gn_with_woe.name, gn_with_woe.gn_id, woe_with_gn.woe_id, woe_with_gn.gn_id, gn_with_woe.country, checkins
 	gn_with_woe.gn_id as gn_id, woe_with_gn.woe_id as woe_id, gn_with_woe.woe_id as woe_id_maybe, woe_with_gn.gn_id as gn_id_maybe, gn_with_woe.name as gn_name, gn_with_woe.asciiname as gn_asciiname, gn_with_woe.country as gn_country, gn_with_woe.admin1 as gn_admin1, gn_with_woe.admin2 as gn_admin2, gn_with_woe.population as gn_population, gn_with_woe.fclass as gn_fclass, gn_with_woe.fcode as gn_fcode, woe_with_gn.name as woe_name, woe_with_gn.name as name, woe_with_gn.english_name as woe_name_en, woe_with_gn.placetype, woe_with_gn.iso, woe_with_gn.language, woe_with_gn.parent_id, woe_with_gn.woe_locality, woe_with_gn.woe_lau, woe_with_gn.woe_adm2, woe_with_gn.woe_adm1, woe_with_gn.woe_adm0, woe_with_gn.name_locality, woe_with_gn.name_lau, woe_with_gn.name_adm2, woe_with_gn.name_adm1, woe_with_gn.name_adm0, woe_with_gn.gns_id, woe_with_gn.accuracy, woe_with_gn.gn_matcht as gn_matchtype, woe_with_gn.spatial_ac as spatial_accuracy, woe_with_gn.woe_funk, woe_with_gn.photos_again as photos, woe_with_gn.photos_again_aggregate as photos_all, woe_with_gn.photos_children_places as woe_members, woe_with_gn.geom as photos_geom, gn_with_woe.checkins as checkins, gn_with_woe.the_geom as checkins_geom
FROM 
 	gn_with_woe
FULL OUTER JOIN
 	woe_with_gn
ON
 	gn_with_woe.woe_id = woe_with_gn.woe_id AND
 	gn_with_woe.gn_id = woe_with_gn.gn_id);

-- http://www.kindle-maps.com/blog/retrospectivly-adding-a-unique-primary-id-column-to-a-table-in-postgresql.html
CREATE SEQUENCE qs_ids2;
ALTER TABLE quattroshapes_gazetteer ADD qs_id INT UNIQUE;
UPDATE quattroshapes_gazetteer SET qs_id = NEXTVAL('qs_ids2');

ALTER TABLE quattroshapes_gazetteer ADD COLUMN checkins_index float;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN photos_index float;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN photos_all_index float;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN checkins_rank int;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN photos_rank int;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN photos_all_rank int;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN population_rank int;

SELECT max(photos), stddev_pop(photos) FROM quattroshapes_gazetteer;
--  max  |    stddev_pop     
---------+-------------------
-- 50015 | 1645.364073003709

SELECT max(photos_all), stddev_pop(photos_all) FROM quattroshapes_gazetteer;
--   max    |   stddev_pop   
------------+----------------
-- 46598243 | 75209.47951609


UPDATE quattroshapes_gazetteer SET photos_index = round(1.0 * photos / (1645*3) * 1000) WHERE photos > 0;
UPDATE quattroshapes_gazetteer SET photos_all_index = round(1.0 * photos_all / (75209*3) * 1000.0) WHERE photos_all > 0;

UPDATE quattroshapes_gazetteer SET checkins_index = 1 WHERE checkins_index = 0 and checkins > 0;
UPDATE quattroshapes_gazetteer SET photos_index = 1 WHERE photos_index = 0 and photos > 0;
UPDATE quattroshapes_gazetteer SET photos_all_index = 1 WHERE photos_all_index = 0 and photos_all > 0;

UPDATE quattroshapes_gazetteer SET checkins_index = 1000 WHERE checkins_index > 1000;
UPDATE quattroshapes_gazetteer SET photos_index = 1000 WHERE photos_index > 1000;
UPDATE quattroshapes_gazetteer SET photos_all_index = 1000 WHERE photos_all_index > 1000;


SELECT AddGeometryColumn('quattroshapes_gazetteer', 'blended_geom', 4326, 'POINT', 2, true);

UPDATE quattroshapes_gazetteer SET blended_geom = checkins_geom where checkins_geom IS NOT NULL;
UPDATE quattroshapes_gazetteer SET blended_geom = photos_geom where checkins_geom IS NULL;

SELECT AddGeometryColumn('quattroshapes_gazetteer', 'blended_geom_gp', 4326, 'POINT', 2, true);

UPDATE quattroshapes_gazetteer SET blended_geom_gp = photos_geom where photos_geom IS NOT NULL;
UPDATE quattroshapes_gazetteer SET blended_geom_gp = checkins_geom where photos_geom IS NULL;

-- where there wasn't a value in GeoPlanet side of the join, let's fill in with Geonames
UPDATE quattroshapes_gazetteer SET name = gn_name where name IS NULL;


--ALTER TABLE quattroshapes_gazetteer ADD COLUMN poprank smallint;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN scalerank smallint;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN natscale smallint;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN adm0cap numeric;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN featurecla character varying(50);
ALTER TABLE quattroshapes_gazetteer ADD COLUMN worldcity smallint;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN megacity smallint;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN metro_core smallint;
ALTER TABLE quattroshapes_gazetteer ADD COLUMN micro_core smallint;

-- the combo file has two different columns for unique ID, normalize them
UPDATE 
	pop12_comp_dedup_merge 
SET 
	geonameid = ï»¿geon
WHERE
	geonameid = 0;

-- make sure there is a difference between 0 and null (-99)
UPDATE 
	quattroshapes_gazetteer 
SET 
--	poprank = -99,
	scalerank = -99,
	natscale = -99;

-- set many attributes for the gazetteer of the main file with 135k features.
UPDATE 
	quattroshapes_gazetteer 
SET 
--	poprank = pop12_comp_dedup_merge.poprank,
	scalerank = pop12_comp_dedup_merge.scalerank,
	natscale = pop12_comp_dedup_merge.natrlScl,
	adm0cap = pop12_comp_dedup_merge.adm0cap,
	featurecla = pop12_comp_dedup_merge.featurecla,
	worldcity = pop12_comp_dedup_merge.worldcity,
	megacity = pop12_comp_dedup_merge.megacity,
	metro_core = pop12_comp_dedup_merge.metro_core
FROM
	pop12_comp_dedup_merge
WHERE
	gn_id = pop12_comp_dedup_merge.geonameid;

-- redo this (not sure it's necc twice)
UPDATE 
	quattroshapes_gazetteer 
SET 
--	poprank = pop12_comp_dedup_merge.poprank,
	scalerank = pop12_comp_dedup_merge.scalerank,
	natscale = pop12_comp_dedup_merge.natrlScl
FROM
	pop12_comp_dedup_merge
WHERE
	gn_id = pop12_comp_dedup_merge.geonameid;

-- prefer the population rank from my edited 135k features over GN population derived values
UPDATE 
	quattroshapes_gazetteer 
SET 
	population_rank = poprank
WHERE
	population_rank < poprank;


-- version 2.0 of Natural Earth had better scale ranks
UPDATE 
	quattroshapes_gazetteer 
SET 
	poprank = ne_10m_populated_places.rank_max,
	scalerank = ne_10m_populated_places.scalerank,
	natscale = ne_10m_populated_places.natscale
FROM
	ne_10m_populated_places
WHERE
	quattroshapes_gazetteer.gn_id = ne_10m_populated_places.geonameid;


UPDATE 
	quattroshapes_gazetteer 
SET 
	micro_core = 1,
	metro_core = 0
FROM
	pop12_comp_dedup_merge
WHERE
	gn_id = pop12_comp_dedup_merge.geonameid AND
	pop12_comp_dedup_merge.metro_type = 'micro';


UPDATE 
	quattroshapes_gazetteer 
SET 
	gn_population = pop12_comp_dedup_merge.population
FROM
	pop12_comp_dedup_merge
WHERE
	gn_id = pop12_comp_dedup_merge.geonameid AND
	gn_population IS NULL;

UPDATE 
	quattroshapes_gazetteer 
SET 
	gn_population = pop12_comp_dedup_merge.pop_2000
FROM
	pop12_comp_dedup_merge
WHERE
	gn_id = pop12_comp_dedup_merge.geonameid AND
	gn_population IS NULL;

UPDATE 
	quattroshapes_gazetteer 
SET 
	gn_population = pop12_comp_dedup_merge.epspop
FROM
	pop12_comp_dedup_merge
WHERE
	gn_id = pop12_comp_dedup_merge.geonameid AND
	gn_population IS NULL;

UPDATE 
	quattroshapes_gazetteer 
SET 
	metro_core = 1
FROM
	us_admin_2_counties_d10m_d
WHERE
	gn_id = us_admin_2_counties_d10m_d.gn1n AND
	us_admin_2_counties_d10m_d.metro = 1;

UPDATE 
	quattroshapes_gazetteer 
SET 
	micro_core = 1
FROM
	us_admin_2_counties_d10m_d
WHERE
	gn_id = us_admin_2_counties_d10m_d.gn1n AND
	us_admin_2_counties_d10m_d.micro = 1;

UPDATE quattroshapes_gazetteer
SET population_rank = CASE
	WHEN gn_population > 15000000 THEN 15
	WHEN gn_population > 10000000 THEN 14
	WHEN gn_population > 5000000 THEN 13
	WHEN gn_population > 1000000 THEN 12
	WHEN gn_population > 500000 THEN 11
	WHEN gn_population > 200000 THEN 10
	WHEN gn_population > 100000 THEN 9
	WHEN gn_population > 50000 THEN 8
	WHEN gn_population > 20000 THEN 7 
	WHEN gn_population > 10000 THEN 6
	WHEN gn_population > 5000 THEN 5
	WHEN gn_population > 2000 THEN 4
	WHEN gn_population > 1000 THEN 3
	WHEN gn_population > 200 THEN 2
	WHEN gn_population > 0 THEN 1
	ELSE 0
 END;

UPDATE quattroshapes_gazetteer
SET photos_rank = CASE
	WHEN photos > 42000 THEN 30
	WHEN photos > 30000 THEN 29
	WHEN photos > 22000 THEN 28
	WHEN photos > 15000 THEN 27
	WHEN photos > 10500 THEN 26
	WHEN photos > 6800 THEN 25
	WHEN photos > 4850 THEN 24
	WHEN photos > 4300 THEN 23
	WHEN photos > 3850 THEN 22
	WHEN photos > 3500 THEN 21
	WHEN photos > 3050 THEN 20
	WHEN photos > 2750 THEN 19
	WHEN photos > 2500 THEN 18
	WHEN photos > 2250 THEN 17
	WHEN photos > 2050 THEN 16
	WHEN photos > 1850 THEN 15
	WHEN photos > 1650 THEN 14
	WHEN photos > 1500 THEN 13
	WHEN photos > 1250 THEN 12
	WHEN photos > 1000 THEN 11
	WHEN photos > 850 THEN 10
	WHEN photos > 750 THEN 9
	WHEN photos > 550 THEN 8
	WHEN photos > 450 THEN 7 
	WHEN photos > 350 THEN 6
	WHEN photos > 250 THEN 5
	WHEN photos > 150 THEN 4
	WHEN photos > 75 THEN 3
	WHEN photos > 25 THEN 2
	WHEN photos > 0 THEN 1
	ELSE 0
 END;


UPDATE quattroshapes_gazetteer
SET photos_all_rank = CASE
	WHEN photos_all > 600000 THEN 30
	WHEN photos_all > 500000 THEN 29
	WHEN photos_all > 375000 THEN 28
	WHEN photos_all > 250000 THEN 27
	WHEN photos_all > 73000 THEN 26
	WHEN photos_all > 55000 THEN 25
	WHEN photos_all > 44000 THEN 24
	WHEN photos_all > 33500 THEN 23
	WHEN photos_all > 25000 THEN 22
	WHEN photos_all > 20000 THEN 21
	WHEN photos_all > 18000 THEN 20
	WHEN photos_all > 15000 THEN 19
	WHEN photos_all > 13000 THEN 18
	WHEN photos_all > 11500 THEN 17
	WHEN photos_all > 10000 THEN 16
	WHEN photos_all > 6500 THEN 15
	WHEN photos_all > 4900 THEN 14
	WHEN photos_all > 4300 THEN 13
	WHEN photos_all > 3500 THEN 12
	WHEN photos_all > 2800 THEN 11
	WHEN photos_all > 2300 THEN 10
	WHEN photos_all > 1800 THEN 9
	WHEN photos_all > 1500 THEN 8
	WHEN photos_all > 1000 THEN 7 
	WHEN photos_all > 750 THEN 6
	WHEN photos_all > 300 THEN 5
	WHEN photos_all > 150 THEN 4
	WHEN photos_all > 75 THEN 3
	WHEN photos_all > 25 THEN 2
	WHEN photos_all > 0 THEN 1
	ELSE 0
 END;


-- geoname lat-long locations, then if there is not one, geoplanet / flickr lat-long locations
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quattroshapes_gazetteer_gn_then_gp.shp -nlt POINT \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT name, qs_id, gn_id, woe_id, gn_id_maybe as gn_id_eh, woe_id_maybe as woe_id_eh, featurecla, scalerank, natscale, adm0cap, worldcity, megacity, metro_core, micro_core, gn_name, gn_asciiname as gn_ascii, gn_country, gn_admin1, gn_admin2, gn_population as gn_pop, gn_fclass, gn_fcode, woe_name, woe_name_en as woe_nameen, placetype, iso, language, parent_id, woe_locality as woe_local, woe_lau, woe_adm2, woe_adm1, woe_adm0, name_locality as name_local, name_lau, name_adm2, name_adm1, name_adm0, gns_id, accuracy, gn_matchtype as matchtype, spatial_accuracy as geom_qual, woe_funk, photos, photos_all, woe_members as woemembers, qs_id, checkins_index as checkin_1k, photos_index as photos_1k, photos_all_index as photos_9k, checkins_rank as checkin_sr, photos_rank as photos_sr, photos_all_rank as photos_9r, population_rank as pop_sr, blended_geom FROM quattroshapes_gazetteer"
	
rm -f shp/quattroshapes_gazetteer_gn_then_gp.zip
zip shp/quattroshapes_gazetteer_gn_then_gp.zip shp/quattroshapes_gazetteer_gn_then_gp.*
	
	
-- geoplanet lat-long locations, then if there is not one, geonames lat-long locations
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quattroshapes_gazetteer_gp_then_gn.shp -nlt POINT \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT name, qs_id, gn_id, woe_id, gn_id_maybe as gn_id_eh, woe_id_maybe as woe_id_eh, gn_name, gn_asciiname as gn_ascii, gn_country, gn_admin1, gn_admin2, gn_population as gn_pop, gn_fclass, gn_fcode, woe_name, woe_name_en as woe_nameen, placetype, iso, language, parent_id, woe_locality as woe_local, woe_lau, woe_adm2, woe_adm1, woe_adm0, name_locality as name_local, name_lau, name_adm2, name_adm1, name_adm0, gns_id, accuracy, gn_matchtype as matchtype, spatial_accuracy as geom_qual, woe_funk, photos, photos_all, woe_members as woemembers, checkins_index as checkin_1k, photos_index as photos_1k, photos_all_index as photos_9k, checkins_rank as checkin_sr, photos_rank as photos_sr, photos_all_rank as photos_9r, population_rank as pop_sr, blended_geom_gp FROM quattroshapes_gazetteer"

rm -f shp/quattroshapes_gazetteer_gp_then_gn.zip
zip shp/quattroshapes_gazetteer_gp_then_gn.zip shp/quattroshapes_gazetteer_gp_then_gn.*

	
-- geoname lat-long locations, then if there is not one, geoplanet / flickr lat-long locations
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quattroshapes_gazetteer_gn_then_gp_with_content.shp -nlt POINT \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT name, qs_id, gn_id, woe_id, gn_population as gn_pop, placetype, gn_fcode, name_adm1, gn_country, woe_adm0, name_adm0, photos, photos_all, checkins_index as checkin_1k, photos_index as photos_1k, photos_all_index as photos_9k, checkins_rank as checkin_sr, photos_rank as photos_sr, photos_all_rank as photos_9r, population_rank as pop_sr, blended_geom FROM quattroshapes_gazetteer WHERE checkins > 0 or photos > 0 or gn_population > 0"

rm shp/quattroshapes_gazetteer_gn_then_gp_with_content.zip
zip shp/quattroshapes_gazetteer_gn_then_gp_with_content.zip shp/quattroshapes_gazetteer_gn_then_gp_with_content.*

-- again but for any locality or P class
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quattroshapes_gazetteer_gn_then_gp_locality.shp -nlt POINT \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT name, qs_id, gn_id, woe_id, gn_population as gn_pop, placetype, gn_fcode, name_adm1, gn_country, woe_adm0, name_adm0, photos, photos_all, checkins_index as checkin_1k, photos_index as photos_1k, photos_all_index as photos_9k, checkins_rank as checkin_sr, photos_rank as photos_sr, photos_all_rank as photos_9r, population_rank as pop_sr, blended_geom FROM quattroshapes_gazetteer WHERE placetype = 'Town' OR (gn_fclass = 'P' and gn_fcode != 'P.PPLX')"

rm -f shp/quattroshapes_gazetteer_gn_then_gp_locality.zip
zip shp/quattroshapes_gazetteer_gn_then_gp_locality.zip shp/quattroshapes_gazetteer_gn_then_gp_locality.*




-- geoname lat-long locations
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quattroshapes_gazetteer_gn.shp -nlt POINT \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT gn_id, woe_id, gn_name, gn_asciiname as gn_ascii, gn_country, gn_admin1, gn_population as gn_pop, gn_fclass, gn_fcode, woe_name, woe_name_en as woe_nameen, placetype, iso, language, parent_id, woe_locality as woe_local, woe_lau, woe_adm2, woe_adm1, woe_adm0, name_locality as name_local, name_lau, name_adm2, name_adm1, name_adm0, gns_id, accuracy, gn_matchtype as matchtype, spatial_accuracy as geom_qual, woe_funk, photos, woe_members as woemembers, checkins, qs_id, checkins_geom FROM quattroshapes_gazetteer"

-- geoplanet / flickr lat-long locations
ogr2ogr -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4326 -t_srs EPSG:4326 \
	-overwrite shp/quattroshapes_gazetteer_gp.shp -nlt POINT \
	PG:"host=localhost user=foursquare dbname=foursquare" \
	-sql "SELECT gn_id, woe_id, gn_name, gn_asciiname, gn_country, gn_admin1, gn_population, gn_fclass, gn_fcode, woe_name, woe_name_en, placetype, iso, language, parent_id, woe_locality, woe_lau, woe_adm2, woe_adm1, woe_adm0, name_locality, name_lau, name_adm2, name_adm1, name_adm0, gns_id, accuracy, gn_matchtype, spatial_accuracy, woe_funk, photos, woe_members, checkins, qs_id, photos_geom FROM quattroshapes_gazetteer"