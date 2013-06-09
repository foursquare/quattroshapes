#quattroshapes

_The Global Polygon Gazetteer_

[Foursquare](http://foursquare.com) needs quality place data to power its geocoding engine to ensure the best recommendations. When someone searches for the best coffee in Brooklyn, a simple venue to place point or venue to place bounding box search can result in venues in Manhattan and Jersey City overwhelming the results for Brooklyn. 

To improve recommendations, we have created an authoritative source of polygons around a curated list of places. This gazetteer of non-overlapping polygons provides more relevant results than simple point geometries. 

[View preview images »](https://github.com/foursquare/quattroshapes#preview)

This work is based on foursquare checkins, geo tagged photos from [Flickr](http://flickr.com), an extended version of [Natural Earth](http://naturalearthdata.com), and [open government data](http://brigade.codeforamerica.org/opendata). Concordance is provided between quattroshapes, [geonames.org](http://geonames.org), and [Yahoo! GeoPlanet](http://developer.yahoo.com/geo/geoplanet/) unique IDs in the gazetteer.

The quattroshapes technique calculates the dominant place ID for a given area based on heterogeneous inputs. This work is an extension of [alphashapes](http://code.flickr.net/2008/10/30/the-shape-of-alpha/) and [betashapes](https://github.com/simplegeo/betashapes) (thanks [Aaron](https://github.com/straup) and [Schuyler](https://github.com/schuyler)!) and is used to backfill countries without complete open data.

Geocoding can be the hardest part about going open source - and reverse geocoding is even harder. Reverse geocoding reports the gazetteer place for a latitude and longitude map location or address string and is useful when source data needs to be normalized. This new polygon gazetteer data is used in [TwoFishes](https://github.com/foursquare/twofishes), the coarse splitting geocoder (and reverse geocoder) written in scala from [David Blackman](https://github.com/blackmad/) at foursquare.

The quattroshapes code and resulting 30 gb of data are licensed under [CC-BY](http://creativecommons.org/licenses/by/2.0/), but includes data licensed from many governments around the world. Check the [License](LICENSE.md) for full details and limitations.

Enjoy!

---

##Downloads

Shapefiles are in WGS84 (geographic) projection and UTF-8 character encoding. 

* [quatroshapes admin 0](http://static.quattroshapes.com/qs_adm0.zip) - 106 mb
* [quatroshapes admin 1 regions](http://static.quattroshapes.com/qs_adm1_region.zip) - 17 mb
* [quatroshapes admin 1](http://static.quattroshapes.com/qs_adm1.zip) - 106 mb
* [quatroshapes admin 2 regions](http://static.quattroshapes.com/qs_adm2_region.zip) - 1.5 mb
* [quatroshapes admin 2](http://static.quattroshapes.com/qs_adm2.zip) - 304 mb
* [quatroshapes local admin](http://static.quattroshapes.com/qs_localadmin.zip) - 467 mb
* [quatroshapes localities](http://static.quattroshapes.com/qs_localities.zip) - 420 mb
* [quatroshapes neighborhoods](http://static.quattroshapes.com/qs_neighborhoods.zip) - 32 mb

##Goodies

quatroshapes gazetteer:

* [prefer GeoNames.org lat-lngs](http://static.quattroshapes.com/quattroshapes_gazetteer_gn_then_gp.zip) - 154 mb
* [prefer GeoPlanet + Flickr lat-lngs](http://static.quattroshapes.com/quattroshapes_gazetteer_gp_then_gn.zip) - 154 mb
* [localities only, Geonames.org lat-lngs](http://static.quattroshapes.com/quattroshapes_gazetteer_gn_then_gp_locality.zip) - 46 mb
* [places with population, checkins, or flickr photos, Geonames.org lat-lngs](http://static.quattroshapes.com/quattroshapes_gazetteer_gn_then_gp_with_content.zip) - 34 mb

Other:

* [Natural Earth admin-1](http://static.quattroshapes.com/ne_adm1.zip) - 16 mb, version 3.0.0
* [US State Department HIU admin-0](http://static.quattroshapes.com/ne_ussd_adm0.zip) - 79 mb, re-coded like Natural Earth
* [National Mapping Agency Open Data](http://static.quattroshapes.com/nma.zip) - 7 gb
* [Customized Europe localities](http://static.quattroshapes.com/europe_localities.zip) - 135 mb, mashed-up EuroGeoGraphics urban data and European Environment Agency [UMZ](http://www.eea.europa.eu/data-and-maps/data/urban-morphological-zones-2006-umz2006-f3v0) data.
* [GeoPlanet voronoi diagrams](http://static.quattroshapes.com/geoplanet_voronoi.zip) - 198 mb includes adm0, adm1, adm2, localadmin & localities.

 
##Preview

**Administrative level 1**: 
_(below) States and provinces in orange; regions shown in red. Mix of national mapping agency and Natural Earth._

![qs_adm1](images/qs_adm1.png)

**Administrative level 2**: 
_(below) Counties in bright blue; regions shown in dark blue. National mapping agency data._

![qs_adm2](images/qs_adm2.png)

**Local administrative level**: 
_(below) In green. This level of government assumes municipal type control over the central town and surrounding countryside. National mapping agency data._

![qs_localadmin](images/qs_localadmin.png)

**Localities**: 
_(below) In yellow. In the USA this is the smallest unit of government with legal boundaries. For most other countries the localities here are informal parts of local administrative areas. Mix of national mapping agency, quattroshapes enumeration using foursquare checkins & custom data._

![qs_localities](images/qs_localities.png)

**Administrative level 0**: 
_(below) In gray. Mix of national mapping agency and US State Department data._

![qs_adm0](images/qs_adm0.png)

**Neighborhoods**: 
_(below) In purple. Quattroshape enumeration from geo tagged photos in Flickr using GeoPlanet hierarchy._

![qs_neighborhoods](images/qs_neighborhoods.png)

**Gazetteer**: 
_(below) In light purple. Over 1 million administrative and populated places with around 800,000 having concordance between GeoNames.org and Yahoo! GeoPlanet WOE unique IDs._

![qs_gazetteer](images/qs_gazetteer.png)
