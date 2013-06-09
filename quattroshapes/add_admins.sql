ALTER TABLE geoplanet_places ADD COLUMN woe_locality bigint; 
ALTER TABLE geoplanet_places ADD COLUMN woe_lau bigint; 
ALTER TABLE geoplanet_places ADD COLUMN woe_adm2 bigint; 
ALTER TABLE geoplanet_places ADD COLUMN woe_adm1 bigint; 
ALTER TABLE geoplanet_places ADD COLUMN woe_adm0 bigint; 


ALTER TABLE geoplanet_places ADD COLUMN name_locality character varying (255);
ALTER TABLE geoplanet_places ADD COLUMN name_lau character varying (255);
ALTER TABLE geoplanet_places ADD COLUMN name_adm2 character varying (255);
ALTER TABLE geoplanet_places ADD COLUMN name_adm1 character varying (255);
ALTER TABLE geoplanet_places ADD COLUMN name_adm0 character varying (255);



-- woe_id             | integer              | not null
-- iso                | character varying(2) | not null
-- state_woe_id       | integer              | not null
-- county_woe_id      | integer              | not null
-- local_admin_woe_id | integer              | not null
-- country_woe_id     | integer              | not null
-- continent_woe_id   | integer              | not null


-- This will work for localities on up, but not for Suburbs

UPDATE 
	geoplanet_places
SET 
	woe_locality = geoplanet_admins.woe_id,
	woe_lau = geoplanet_admins.local_admin_woe_id,
	woe_adm2 = geoplanet_admins.county_woe_id,
	woe_adm1 = geoplanet_admins.state_woe_id,
	woe_adm0 = geoplanet_admins.country_woe_id
FROM 
	geoplanet_admins
WHERE 
	geoplanet_admins.woe_id = geoplanet_places.woe_id;


--Works except for NYC

UPDATE 
	geoplanet_places
SET 
	woe_locality = parent_id
WHERE 
	placetype = 'Suburb';
	
	
UPDATE 
	geoplanet_places
SET 
	woe_locality = woe_id
WHERE 
	placetype = 'Town';

UPDATE 
	geoplanet_places
SET 
	woe_lau = woe_id
WHERE 
	placetype = 'LocalAdmin';
	
UPDATE 
	geoplanet_places
SET 
	woe_adm2 = woe_id
WHERE 
	placetype = 'County';
	
UPDATE 
	geoplanet_places
SET 
	woe_adm1 = woe_id
WHERE 
	placetype = 'State';

UPDATE 
	geoplanet_places
SET 
	woe_adm0 = woe_id
WHERE 
	placetype = 'Country';



-- ALTER TABLE geoplanet_places ADD COLUMN woe_locality bigint; 
-- ALTER TABLE geoplanet_places ADD COLUMN woe_lau bigint; 
-- ALTER TABLE geoplanet_places ADD COLUMN woe_adm2 bigint; 
-- ALTER TABLE geoplanet_places ADD COLUMN woe_adm1 bigint; 
-- ALTER TABLE geoplanet_places ADD COLUMN woe_adm0 bigint; 


-- ALTER TABLE geoplanet_places ADD COLUMN name_locality character varying (255);
-- ALTER TABLE geoplanet_places ADD COLUMN name_lau character varying (255);
-- ALTER TABLE geoplanet_places ADD COLUMN name_adm2 character varying (255);
-- ALTER TABLE geoplanet_places ADD COLUMN name_adm1 character varying (255);
-- ALTER TABLE geoplanet_places ADD COLUMN name_adm0 character varying (255);



WITH placename AS (
	SELECT 
		name, woe_id
	FROM 
		geoplanet_places
)
UPDATE 
	geoplanet_places
SET 
	name_locality = placename.name
FROM 	
	placename
WHERE 
	geoplanet_places.woe_locality = placename.woe_id;	


	
WITH placename AS (
	SELECT 
		name, woe_id
	FROM 
		geoplanet_places
)
UPDATE 
	geoplanet_places
SET 
	name_lau = placename.name
FROM 	
	placename
WHERE 
	geoplanet_places.woe_lau = placename.woe_id;	
	

--http://stackoverflow.com/questions/9643859/postgres-missing-from-clause-entry-error-on-query-with-with-clause

WITH placename AS (
	SELECT 
		name, woe_id
	FROM 
		geoplanet_places
)
UPDATE 
	geoplanet_places
SET 
	name_adm2 = placename.name
FROM 	
	placename
WHERE 
	geoplanet_places.woe_adm2 = placename.woe_id;



WITH placename AS (
	SELECT 
		name, woe_id
	FROM 
		geoplanet_places
)
UPDATE 
	geoplanet_places
SET 
	name_adm1 = placename.name
FROM 	
	placename
WHERE 
	geoplanet_places.woe_adm1 = placename.woe_id;
	

	

WITH placename AS (
	SELECT 
		name, woe_id
	FROM 
		geoplanet_places
)
UPDATE 
	geoplanet_places
SET 
	name_adm0 = placename.name
FROM 	
	placename
WHERE 
	geoplanet_places.woe_adm0 = placename.woe_id;