all: \
	all_localities.shp \
	all_localadmin.shp \
	all_adm0.shp \
	all_adm1_region.shp \
	all_adm1.shp \
	all_adm2_region.shp \
	all_adm2.shp
	
	touch all

all-zips: \
	all_localities.zip \
	all_localadmin.zip \
	all_localadmin.zip \
	all_adm0.zip \
	all_adm1_region.zip \
	all_adm1.zip \
	all_adm2_region.zip \
	all_adm2.zip 

	touch all-zips
	
all.zip: \
	all_localities.zip \
	all_localadmin.zip \
	all_localadmin.zip \
	all_adm0.zip \
	all_adm1_region.zip \
	all_adm1.zip \
	all_adm2_region.zip \
	all_adm2.zip 

	rm -f all.zip
	zip all.zip all_*.shp all_*.dbf all_*.shx all_*.prj all_*.cpg

all_localities.zip:
	rm -f all_localities.zip
	zip all_localities.zip all_localities.*
	
all_localadmin.zip:
	rm -f all_localadmin.zip
	zip all_localadmin.zip all_localadmin.*
	
all_adm0.zip:
	rm -f all_adm0.zip
	zip all_adm0.zip all_adm0.*

all_adm1_region.zip:
	rm -f all_adm1_region.zip
	zip all_adm1_region.zip all_adm1_region.*

all_adm1.zip:
	rm -f all_adm1.zip
	zip all_adm1.zip all_adm1.*

all_adm2_region.zip:
	rm -f all_adm2_region.zip
	zip all_adm2_region.zip all_adm2_region.*

all_adm2.zip:
	rm -f all_adm2.zip
	zip all_adm2.zip all_adm2.*


all_localities.shp: \
	aus_localities.shp \
	bra_localities.shp \
	can_localities.shp \
	eu_localities.shp \
	nzl_localities.shp \
	pri_localities.shp \
	pse_localities.shp \
	usa_localities.shp \
	zaf_localities.shp \
	mex_localities.shp \
	rus_localities.shp \
	idn_localities_qs.shp \
	mys_localities_qs.shp \
	tha_localities_qs.shp \
	kor_localities_qs.shp \
	twn_localities_qs.shp \
	chn_localities_qs.shp \
	ind_localities_qs.shp \
	jpn_localities_qs.shp \
	sgp_localities_qs.shp
	#tur_localities_qs.shp \
	#gbr_localities_qs.shp
	#tur_localities.shp \
	#gbr_localities.shp \
	#chl_localities.shp \
	#mex_localities.shp \
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_localities.shp templates/template_localities.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp usa_localities.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp can_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp eu_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp nzl_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp pri_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp pse_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp zaf_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp aus_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp bra_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp mex_localities.shp
	#ogr2ogr -f "Esri Shapefile" -append all_localities.shp mex_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp rus_localities.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp chl_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp idn_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp mys_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp tha_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp kor_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp twn_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp chn_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp ind_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp jpn_localities_qs.shp
	ogr2ogr -f "Esri Shapefile" -append all_localities.shp sgp_localities_qs.shp
	#ogr2ogr -f "Esri Shapefile" -append all_localities.shp tur_localities_qs.shp
	#ogr2ogr -f "Esri Shapefile" -append all_localities.shp gbr_localities_qs.shp
	#ogr2ogr -f "Esri Shapefile" -append all_localities.shp rus_localities_qs.shp
	
all_localadmin.shp: \
	aus_localadmin.shp \
	bra_localadmin.shp \
	che_localadmin.shp \
	esp_localadmin.shp \
	fra_localadmin.shp \
	gbr_localadmin.shp \
	ita_localadmin.shp \
	lie_localadmin.shp \
	nld_localadmin.shp \
	usa_localadmin.shp
	
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_localadmin.shp templates/template_localadmin.shp
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp aus_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp bra_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp che_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp esp_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp fra_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp gbr_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp ita_localadmin.shp	
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp lie_localadmin.shp
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp nld_localadmin.shp
	ogr2ogr -f "Esri Shapefile" -append all_localadmin.shp usa_localadmin.shp

all_adm2_region.shp: \
	deu_adm2_region.shp \
	fra_adm2_region.shp
	
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_adm2_region.shp templates/template_adm2_region.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm2_region.shp deu_adm2_region.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm2_region.shp fra_adm2_region.shp	

all_adm2.shp: \
	aus_adm2.shp \
	aut_adm2.shp \
	bel_adm2.shp \
	bra_adm2.shp \
	che_adm2.shp \
	chl_adm2.shp \
	deu_adm2.shp \
	fra_adm2.shp \
	idn_adm2.shp \
	ltu_adm2.shp \
	mex_adm2.shp \
	nzl_adm2.shp \
	pol_adm2.shp \
	pri_adm2.shp \
	svk_adm2.shp \
	usa_adm2.shp \
	ukr_adm2.shp \
	zaf_adm2.shp
	
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_adm2.shp templates/template_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp aus_adm2.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp aut_adm2.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp bel_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp bra_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp che_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp chl_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp deu_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp fra_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp idn_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp ltu_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp mex_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp nzl_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp pol_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp pri_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp svk_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp usa_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp ukr_adm2.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm2.shp zaf_adm2.shp
	
all_adm1.shp: \
	aus_adm1.shp \
	aut_adm1.shp \
	bel_adm1.shp \
	bgr_adm1.shp \
	bra_adm1.shp \
	can_adm1.shp \
	chl_adm1.shp \
	che_adm1.shp \
	cyp_adm1.shp \
	cze_adm1.shp \
	deu_adm1.shp \
	dnk_adm1.shp \
	esp_adm1.shp \
	est_adm1.shp \
	fin_adm1.shp \
	fra_adm1.shp \
	gbr_adm1.shp \
	gib_adm1.shp \
	grc_adm1.shp \
	grl_adm1.shp \
	hrv_adm1.shp \
	hun_adm1.shp \
	idn_adm1.shp \
	irl_adm1.shp \
	ita_adm1.shp \
	lie_adm1.shp \
	ltu_adm1.shp \
	lva_adm1.shp \
	mco_adm1.shp \
	mda_adm1.shp \
	mex_adm1.shp \
	mlt_adm1.shp \
	nld_adm1.shp \
	nor_adm1.shp \
	nzl_adm1.shp \
	pol_adm1.shp \
	pri_adm1.shp \
	prt_adm1.shp \
	pse_adm1.shp \
	rou_adm1.shp \
	rus_adm1.shp \
	srb_adm1.shp \
	svk_adm1.shp \
	swe_adm1.shp \
	usa_adm1.shp \
	ukr_adm1.shp \
	vat_adm1.shp \
	zaf_adm1.shp \
	ne_adm1.shp
	
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_adm1.shp templates/template_adm1.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp ne_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp aus_adm1.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp aut_adm1.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp bel_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp bgr_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp bra_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp can_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp chl_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp che_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp cyp_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp cze_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp deu_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp dnk_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp esp_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp est_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp fin_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp fra_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp gbr_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp gib_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp grc_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp grl_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp hrv_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp hun_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp irl_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp ita_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp lie_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp ltu_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp lva_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp mco_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp mda_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp mex_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp mlt_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp nld_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp nor_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp nzl_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp pol_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp pri_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp prt_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp pse_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp rou_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp rus_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp srb_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp svk_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp swe_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp usa_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp ukr_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp vat_adm1.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1.shp zaf_adm1.shp
			
all_adm1_region.shp: \
	bel_adm1_region.shp \
	esp_adm1_region.shp \
	fin_adm1_region.shp \
	fra_adm1_region.shp \
	gbr_adm1_region.shp \
	hun_adm1_region.shp \
	ita_adm1_region.shp \
	srb_adm1_region.shp

	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_adm1_region.shp templates/template_adm1_region.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp bel_adm1_region.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp esp_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp fin_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp fra_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp gbr_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp hun_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp ita_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm1_region.shp srb_adm1_region.shp

all_adm0.shp: \
	aus_adm0.shp \
	ald_adm0.shp \
	aut_adm0.shp \
	bel_adm0.shp \
	bgr_adm0.shp \
	bra_adm0.shp \
	can_adm0.shp \
	che_adm0.shp \
	chl_adm0.shp \
	cze_adm0.shp \
	deu_adm0.shp \
	dnk_adm0.shp \
	esp_adm0.shp \
	est_adm0.shp \
	fin_adm0.shp \
	fra_adm0.shp \
	fro_adm0.shp \
	gbr_adm0.shp \
	geo_adm0.shp \
	gib_adm0.shp \
	grc_adm0.shp \
	grl_adm0.shp \
	hrv_adm0.shp \
	hun_adm0.shp \
	irl_adm0.shp \
	isl_adm0.shp \
	ita_adm0.shp \
	kos_adm0.shp \
	lie_adm0.shp \
	ltu_adm0.shp \
	lux_adm0.shp \
	lva_adm0.shp \
	mco_adm0.shp \
	mda_adm0.shp \
	mex_adm0.shp \
	mlt_adm0.shp \
	nld_adm0.shp \
	nor_adm0.shp \
	nzl_adm0.shp \
	pol_adm0.shp \
	pri_adm0.shp \
	prt_adm0.shp \
	pse_adm0.shp \
	rou_adm0.shp \
	smr_adm0.shp \
	srb_adm0.shp \
	svk_adm0.shp \
	svn_adm0.shp \
	swe_adm0.shp \
	usa_adm0.shp \
	ukr_adm0.shp \
	zaf_adm0.shp \
	ussd_adm0.shp

	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" all_adm0.shp templates/template_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp ussd_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp aut_adm0.shp	
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp ald_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp aus_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp bel_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp bgr_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp bra_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp can_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp che_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp chl_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp cze_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp deu_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp dnk_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp esp_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp est_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp fin_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp fra_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp fro_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp gbr_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp geo_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp gib_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp grc_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp grl_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp hrv_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp hun_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp irl_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp isl_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp ita_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp kos_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp lie_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp ltu_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp lux_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp lva_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp mco_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp mda_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp mex_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp mlt_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp nld_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp nor_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp nzl_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp pol_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp pri_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp prt_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp pse_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp rou_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp srb_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp smr_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp svk_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp svn_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp swe_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp usa_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp ukr_adm0.shp
	ogr2ogr -f "Esri Shapefile" -append all_adm0.shp zaf_adm0.shp
    

dissolve-prep: \
	usa_adm0.shp \
	bra_adm0.shp \
	bra_adm1.shp \
	aus_adm0.shp \
	aus_adm1.shp \
	aus_adm2.shp \
	rus_adm0.shp \
	nzl_adm0.shp \
	che_adm0.shp \
	che_adm1.shp \
	idn_adm0.shp \
	idn_adm1.shp \
	idn_adm2.shp \
	chl_adm1.shp \
	chl_adm0.shp \
	pse_adm0.shp \
	zaf_adm1.shp \
	zaf_adm1.shp \
	gbr_adm1_region.shp \
	bel_adm1_region.shp \
	fin_adm1_region.shp \
	fra_adm1_region.shp \
	hun_adm1_region.shp \
	srb_adm1_region.shp \
	aut_adm1.shp \
	bel_adm1.shp \
	deu_adm1.shp \
	srb_adm1.shp \
	svk_adm1.shp \
	pol_adm1.shp \
	ukr_adm1.shp \
	ltu_adm1.shp \
	aut_adm0.shp \
	bel_adm0.shp \
	deu_adm0.shp \
	fin_adm0.shp \
	fra_adm0.shp \
	hun_adm0.shp \
	ltu_adm0.shp \
	pol_adm0.shp \
	srb_adm0.shp \
	svk_adm0.shp \
	ukr_adm0.shp \
	cze_adm0.shp \ 
	dnk_adm0.shp \ 
	esp_adm0.shp \ 
	est_adm0.shp \ 
	fin_adm0.shp \ 
	gbr_adm0.shp \ 
	grc_adm0.shp \ 
	grl_adm0.shp \ 
	hrv_adm0.shp \ 
	irl_adm0.shp \ 
	isl_adm0.shp \ 
	ita_adm0.shp \ 
	kos_adm0.shp \ 
	lva_adm0.shp \ 
	mda_adm0.shp \ 
	nld_adm0.shp \ 
	nor_adm0.shp \ 
	prt_adm0.shp \ 
	rou_adm0.shp
	
	rm -f dissolvers/*.shp dissolvers/*.shx dissolvers/*.dbf dissolvers/*.prj dissolvers/*.cpg
		
	cp usa_adm0.* dissolvers/
	cp bra_adm0.* dissolvers/
	cp bra_adm1.* dissolvers/
	cp brg_adm0.* dissolvers/ 
	cp aus_adm0.* dissolvers/
	cp aus_adm1.* dissolvers/
	cp aus_adm2.* dissolvers/
	cp rus_adm0.* dissolvers/
	cp mex_adm0.* dissolvers/
	cp nzl_adm0.* dissolvers/
	cp che_adm0.* dissolvers/
	cp che_adm1.* dissolvers/
	cp idn_adm0.* dissolvers/
	cp idn_adm1.* dissolvers/
	cp idn_adm2.* dissolvers/
	cp chl_adm1.* dissolvers/
	cp chl_adm0.* dissolvers/
	cp pse_adm0.* dissolvers/
	cp zaf_adm1.* dissolvers/
	cp zaf_adm1.* dissolvers/
	cp gbr_adm1_region.* dissolvers/
	cp bel_adm1_region.* dissolvers/
	cp fin_adm1_region.* dissolvers/
	cp fra_adm1_region.* dissolvers/
	cp hun_adm1_region.* dissolvers/
	cp srb_adm1_region.* dissolvers/
	cp aut_adm1.* dissolvers/
	cp bel_adm1.* dissolvers/
	cp deu_adm1.* dissolvers/
	cp srb_adm1.* dissolvers/
	cp svk_adm1.* dissolvers/
	cp pol_adm1.* dissolvers/
	cp ukr_adm1.* dissolvers/
	cp ltu_adm1.* dissolvers/
	
	cp aut_adm0.* dissolvers/
	cp bel_adm0.* dissolvers/
	cp deu_adm0.* dissolvers/
	cp fin_adm0.* dissolvers/
	cp fra_adm0.* dissolvers/
	cp hun_adm0.* dissolvers/
	cp ltu_adm0.* dissolvers/
	cp pol_adm0.* dissolvers/
	cp srb_adm0.* dissolvers/
	cp svk_adm0.* dissolvers/
	cp ukr_adm0.* dissolvers/
	
	cp brg_adm0.* dissolvers/
	cp cze_adm0.* dissolvers/
	cp dnk_adm0.* dissolvers/
	cp esp_adm0.* dissolvers/
	cp est_adm0.* dissolvers/
	cp fin_adm0.* dissolvers/
	cp gbr_adm0.* dissolvers/
	cp grc_adm0.* dissolvers/
	cp grl_adm0.* dissolvers/
	cp hrv_adm0.* dissolvers/
	cp irl_adm0.* dissolvers/
	cp isl_adm0.* dissolvers/
	cp ita_adm0.* dissolvers/
	cp kos_adm0.* dissolvers/
	cp lva_adm0.* dissolvers/
	cp mda_adm0.* dissolvers/
	cp nld_adm0.* dissolvers/
	cp nor_adm0.* dissolvers/
	cp prt_adm0.* dissolvers/
	cp rou_adm0.* dissolvers/
	cp swe_adm0.* dissolvers/
			

ald: \
	ald_adm0.shp
	touch ald

aus: \
	aus_adm0.shp \
	aus_adm1.shp \
	aus_adm2.shp \
	aus_localadmin.shp \
	aus_localities.shp
	touch aus

aut: \
	aut_adm0.shp \
	aut_adm1.shp \
	aut_adm2.shp
	touch aut

bel: \
	bel_adm0.shp \
	bel_adm1_region.shp \
	bel_adm1.shp \
	bel_adm2.shp
	touch bel

bgr: \
	bgr_adm0.shp \
	bgr_adm1.shp
	touch bgr

bra: \
	bra_adm2.shp \
	bra_adm1.shp \
	bra_adm0.shp \
	bra_localadmin.shp \
	bra_localities.shp
	touch bra

can: \
	can_localities.shp \
	can_adm1.shp \
	can_adm0.shp
	touch can
	
che: \
	che_adm0.shp \
	che_adm1.shp \
	che_localadmin.shp
	touch che

chl: \
	chl_localities.shp \
	chl_adm2.shp \
	chl_adm1.shp \
	chl_adm0.shp
	touch chl
	
cyp: \
	cyp_adm0.shp \
	cyp_adm1.shp
	touch cyp

cze: \
	cze_adm0.shp \
	cze_adm1.shp
	touch cze

deu: \
	src.shp \
	deu_adm1.shp \
	src.shp \
	src.shp
	touch deu

dnk: \
	dnk_adm0.shp \
	dnk_adm1.shp
	touch dnk

esp: \
	esp_localadmin.shp \
	esp_adm1.shp \
	esp_adm1_region.shp \
	esp_adm0.shp \
	touch esp

est: \
	est_adm0.shp \
	est_adm1.shp
	touch est
	
eu: \
	eu_localities.shp
	touch eu
	
fin: \
	fin_adm0.shp \
	fin_adm1_region.shp \
	fin_adm1.shp
	touch fin

fra: \
	fra_localadmin.shp \
	fra_adm2.shp \
	fra_adm1.shp \
	fra_adm1_region.shp \
	src.shp
	touch fra
	
fro: \
	fro_adm0.shp
	touch fro

gbr: \
	gbr_adm0.shp \
	gbr_adm1.shp \
	gbr_adm1_region.shp \
	gbr_localadmin.shp
	touch gbr

geo: \
	geo_adm0.shp
	touch geo
	
grc: \
	grc_adm0.shp \
	grc_adm1.shp
	touch grc

grl: \
	grl_adm0.shp \
	grl_adm1.shp
	touch grl

hun: \
	hun_adm0.shp \
	hun_adm1_region.shp \
	hun_adm1.shp
	touch hun
	
hrv: \
	hrv_adm0.shp \
	hrv_adm1.shp
	touch hrv

idn: \
	idn_adm2.shp \
	idn_adm1.shp \
	idn_adm0.shp
	touch idn
	
irl: \
	irl_adm0.shp \
	irl_adm1.shp
	touch irl

isl: \
	isl_adm0.shp
	touch isl
	
ita: \
	ita_localadmin.shp \
	ita_adm1.shp \
	ita_adm1_region.shp
	ita_adm0.shp \
	touch ita

kos: \
	kos_adm0.shp
	touch kos

ltu: \
	ltu_adm0.shp \
	ltu_adm1.shp \
	ltu_adm2.shp
	touch ltu

lux: \
	lux_adm0.shp
	touch lux

lva: \
	lva_adm0.shp \
	lva_adm1.shp
	touch lva

mda: \
	mda_adm0.shp \
	mda_adm1.shp
	touch mda

mex: \
	mex_localities.shp \
	mex_adm2.shp \
	mex_adm1.shp \
	mex_adm0.shp
	touch mex

nld: \
	nld_localadmin.shp \
	nld_adm1.shp \
	nld_adm0.shp
	touch nld

nor: \
	nor_adm0.shp \
	nor_adm1.shp
	touch nor
	
nzl: \
	nzl_localities.shp \
	nzl_adm2.shp \
	nzl_adm1.shp
	touch nzl
	
pol: \
	pol_adm0.shp \
	pol_adm1.shp \
	pol_adm2.shp
	touch pol

pri: \
	pri_adm0.shp \
	pri_adm1.shp \
	pri_adm2.shp \
	pri_localities.shp
	touch pri

prt: \
	prt_adm0.shp \
	prt_adm1.shp \
	prt_adm0.shp
	touch prt

pse: \
	pse_localities.shp\
	pse_adm1.shp
	touch pse

rou:
	rou_adm0.shp \
	rou_adm1.shp
	touch rou

rus: \
	rus_localities.shp \
	rus_adm1.shp \
	rus_adm0.shp
	touch rus
	
srb: \
	srb_adm0.shp \
	srb_adm1_region.shp \
	srb_adm1.shp
	touch srb

smr: \
	smr_adm0.shp
	touch smr

svk: \
	svk_adm0.shp \
	svk_adm1.shp \
	svk_adm2.shp
	touch svk

svn: \
	svn_adm0.shp
	touch svn
	
swe: \
	swe_adm0.shp \
	swe_adm1.shp
	touch swe

ukr: \
	ukr_adm0.shp \
	ukr_adm1.shp \
	ukr_adm2.shp
	touch ukr

vat: \
	vat_adm0.shp \
	vat_adm1.shp
	touch vat

usa: \
	usa_adm0.shp \
	usa_adm1.shp \
	usa_adm2.shp \
	usa_localadmin.shp \
	usa_localities.shp
	touch usa
		
zaf: \
	zaf_localities.shp \
	zaf_adm2.shp \
	zaf_adm1.shp \
	zaf_adm0.shp
	touch zaf


# UNITED STATES

usa_adm0.shp: raw_downloads/tl_2010_us_state10.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'USA' as qs_adm0_a3, 'United States' as qs_adm0, 'adm0' as qs_level, 'US Census' as qs_source, 'US' as qs_iso_cc, 'United States' as qs_a0 FROM tl_2010_us_state10 WHERE statefp10 != '72'" usa_adm0.shp raw_downloads/tl_2010_us_state10.shp

usa_adm1.shp: raw_downloads/tl_2010_us_state10.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" --config SHAPE_ENCODING "Windows-1252" -lco ENCODING="UTF-8" -sql "SELECT 'USA' as qs_adm0_a3, 'United States' as qs_adm0, 'adm1' as qs_level, 'US Census' as qs_source, name10 as qs_a1, statefp10 as qs_a1_lc, mtfcc10 as qs_type, 'US' as qs_iso_cc, 'United States' as qs_a0 FROM tl_2010_us_state10 WHERE statefp10 != '72'" usa_adm1.shp raw_downloads/tl_2010_us_state10.shp

usa_adm2.shp: \
	raw_downloads/tl_2010_us_county10.shp \
	usa_adm1.shp
	# --config SHAPE_ENCODING WINDOWS-1252
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'USA' as qs_adm0_a3, 'United States' as qs_adm0, 'adm2' as qs_level, 'US Census' as qs_source, src.name10 as qs_a2, src.namelsad10 as qs_a2_alt, src.statefp10 as qs_a1_lc, namefile.qs_a1 as qs_a1, src.geoid10 as qs_a2_lc, src.mtfcc10 as qs_type, 'US' as qs_iso_cc, 'United States' as qs_a0 FROM tl_2010_us_county10 src LEFT JOIN 'usa_adm1.dbf'.usa_adm1 namefile ON src.statefp10 = namefile.qs_a1_lc WHERE src.statefp10 != '72'" usa_adm2.shp raw_downloads/tl_2010_us_county10.shp

usa_localities.shp: usa_adm1.shp
	# --config SHAPE_ENCODING WINDOWS-1252
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'USA' as qs_adm0_a3, 'United States' as qs_adm0, 'locality' as qs_level, 'US Census' as qs_source, src.name as qs_loc, src.namelsad as qs_loc_alt, src.statefp as qs_a1_lc, namefile.qs_a1 as qs_a1, src.geoid as qs_loc_lc, src.placens as qs_loc_lc2, src.mtfcc as qs_type, 'US' as qs_iso_cc, 'United States' as qs_a0 FROM usa_2012_places src LEFT JOIN 'usa_adm1.dbf'.usa_adm1 namefile ON src.statefp = namefile.qs_a1_lc WHERE src.statefp != '72'" usa_localities.shp ../nma/usa/usa_2012_places.shp

usa_localadmin.shp: raw_downloads/usa_localadmin_all.shp \
	usa_adm1.shp \
	usa_adm2.shp \
	raw_downloads/CouSub_2010Census_DP1.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'USA' as qs_adm0_a3, 'US' as qs_iso_cc, 'United States' as qs_adm0, 'United States' as qs_a0, 'localadmin' as qs_level, 'US Census' as qs_source, src.state as qs_a1_lc, namefile.qs_a1 as qs_a1, CONCAT(src.state,src.county) as qs_a2_lc, src.name as qs_la, CONCAT(src.state,src.county,src.cousub) as qs_la_lc, src.geo_id as qs_la_lc2, src.lsad as qs_type FROM usa_localadmin_all src LEFT JOIN 'usa_adm1.dbf'.usa_adm1 namefile ON src.state = namefile.qs_a1_lc" usa_localadmin.shp raw_downloads/usa_localadmin_all.shp
	# add adm2 names
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_iso_cc, qs_adm0, qs_a0, qs_level, qs_source, qs_a1, qs_a2_lc, namefile.qs_a2 as qs_a2, qs_la, qs_la_lc, qs_la_lc2, qs_type, qs_a1_lc FROM usa_localadmin src LEFT JOIN 'usa_adm2.dbf'.usa_adm2 namefile ON src.qs_a2_lc = namefile.qs_a2_lc" usa_localadmin.shp usa_localadmin.shp
	# add populations
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_iso_cc, qs_adm0, qs_a0, qs_level, qs_source, qs_a1, qs_a2_lc, qs_a2, qs_la, qs_la_lc, qs_la_lc2, qs_type, qs_a1_lc, namefile.DP0010001 as qs_pop FROM usa_localadmin src LEFT JOIN 'raw_downloads/CouSub_2010Census_DP1.dbf'.CouSub_2010Census_DP1 namefile ON src.qs_la_lc = namefile.geoid10" usa_localadmin.shp usa_localadmin.shp

	

# PR

pri_adm0.shp: raw_downloads/tl_2010_us_state10.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PRI' as qs_adm0_a3, 'Puerto Rico' as qs_adm0, 'adm0' as qs_level, 'PR' as qs_iso_cc, 'Puerto Rico' as qs_a0, 'US Census' as qs_source  FROM tl_2010_us_state10 WHERE statefp10 = '72'" pri_adm0.shp raw_downloads/tl_2010_us_state10.shp

pri_adm1.shp: raw_downloads/tl_2010_us_state10.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PRI' as qs_adm0_a3, 'Puerto Rico' as qs_adm0, 'adm1' as qs_level, 'US Census' as qs_source, 'PR' as qs_iso_cc, 'Puerto Rico' as qs_a0,name10 as qs_a1, statefp10 as qs_a1_lc, mtfcc10 as qs_type FROM tl_2010_us_state10 WHERE statefp10 = '72'" pri_adm1.shp raw_downloads/tl_2010_us_state10.shp

pri_adm2.shp: \
	raw_downloads/tl_2010_us_county10.shp \
	pri_adm1.shp
	# --config SHAPE_ENCODING WINDOWS-1252
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PRI' as qs_adm0_a3, 'Puerto Rico' as qs_adm0, 'adm2' as qs_level, 'US Census' as qs_source, 'PR' as qs_iso_cc, 'Puerto Rico' as qs_a0, src.name10 as qs_a2, src.namelsad10 as qs_a2_alt, src.statefp10 as qs_a1_lc, namefile.qs_a1 as qs_a1, src.geoid10 as qs_a2_lc, src.mtfcc10 as qs_type FROM tl_2010_us_county10 src LEFT JOIN 'usa_adm1.dbf'.usa_adm1 namefile ON src.statefp10 = namefile.qs_a1_lc WHERE src.statefp10 = '72'" pri_adm2.shp raw_downloads/tl_2010_us_county10.shp

pri_localities.shp: pri_adm1.shp
	# --config SHAPE_ENCODING WINDOWS-1252
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PRI' as qs_adm0_a3, 'Puerto Rico' as qs_adm0, 'locality' as qs_level, 'US Census' as qs_source, 'PR' as qs_iso_cc, 'Puerto Rico' as qs_a0, src.name as qs_loc, src.namelsad as qs_loc_alt, src.statefp as qs_a1_lc, namefile.qs_a1 as qs_a1, src.geoid as qs_loc_lc, src.placens as qs_loc_lc2, src.mtfcc as qs_type FROM usa_2012_places src LEFT JOIN 'pri_adm1.dbf'.pri_adm1 namefile ON src.statefp = namefile.qs_a1_lc WHERE src.statefp = '72'" pri_localities.shp ../nma/usa/usa_2012_places.shp

# UNITED KINGDOM

#gbr_adm1.shp:
#	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT name as qs_a1, code as qs_a1_lc, descriptio as qs_type FROM district_borough_unitary_region" gbr_adm1.shp ../nma/united_kingdom/bdline_gb/Data/district_borough_unitary_region.shp

#United Kingdom SH3, needs Norther Ireland (ND) appended (SH4) - 4 regions

gbr_adm0.shp:
	# Start with Northern Ireland due to long qs_a1_lc
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'GBR' as qs_adm0_a3, 'United Kingdom' as qs_adm0, 'adm0' as qs_level, 'GB' as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN4 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" gbr_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/ND/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -append -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'GBR' as qs_adm0_a3, 'United Kingdom' as qs_adm0, 'adm0' as qs_level, 'EuroGlobalMap' as qs_source, 'GB' as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN2 as qs_a1r_lc, src.SHN3 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" gbr_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/GB/PolbndA.shp
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.DESN as qs_type FROM gbr_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" gbr_adm0.shp gbr_adm0.shp


# Proceed with whole

gbr_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'GBR' as qs_adm0_a3, 'United Kingdom' as qs_adm0, 'adm1_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM gbr_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" gbr_adm1_region.shp gbr_adm0.shp
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.DESN as qs_type FROM gbr_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" gbr_adm1_region.shp gbr_adm1_region.shp
	
gbr_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'GBR' as qs_adm0_a3, 'United Kingdom' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM gbr_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" gbr_adm1.shp gbr_adm1_region.shp
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM gbr_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" gbr_adm1.shp gbr_adm1.shp


gbr_localadmin.shp:
	#Let's setup the basic construct
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -t_srs EPSG:4326 -s_srs EPSG:27700 -sql "SELECT 'GBR' as qs_adm0_a3, 'GB' as qs_iso_cc, 'United Kingdom' as qs_adm0, 'United Kingdom' as qs_a0, 'localadmin' as qs_level, 'UK OS' as qs_source, file_name as qs_a1, name as qs_la, code as qs_la_lc, number as qs_la_lc2, SUBSTR(code,0,1) as qs_a1r_lc, descriptio as qs_type FROM parish_region" gbr_localadmin_tmp.shp ../nma/united_kingdom/bdline_gb/Data/parish_region.shp
	# England is prefix E or prefix null -spat -120059.56 -217878.65 738273.25 577762.31
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -spat -6.84171 49.51701 2.04510735 55.9099265 -sql "SELECT qs_adm0_a3, qs_iso_cc, qs_adm0, qs_a0, qs_level, qs_source, qs_la, qs_la_lc, qs_la_lc2, qs_a1, qs_type, 'England' as qs_a1r, 'GB12000000' as qs_a1r_lc FROM gbr_localadmin_tmp WHERE qs_a1r_lc = 'E' OR (qs_a1r_lc IS NULL AND qs_a1 NOT IN ('SCOTTISH_BORDERS','DUMFRIES_AND_GALLOWAY','SOUTH_AYRSHIRE','EAST_AYRSHIRE','SOUTH_LANARKSHIRE','NORTH_LANARKSHIRE','ARGYLL_AND_BUTE','EAST_DUNBARTONSHIRE','WEST_DUNBARTONSHIRE','WEST_LOTHIAN','CLACKMANNANSHIRE','FALKIRK','FIFE','GLASGOW_CITY','PERTY_AND_KINROSS','INVERCLYDE','NORTH_AYRSHIRE','EAST_RENFREWSHIRE','RENFREWSHIRE','MIDLOTHIAN','STIRLING','EAST_LOTHIAN','CITY_OF_EDINBURGH'))" gbr_localadmin.shp gbr_localadmin_tmp.shp
	# Wales is prefix W
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT qs_adm0_a3, qs_iso_cc, qs_adm0, qs_a0, qs_level, qs_source, qs_la, qs_la_lc, qs_la_lc2, qs_a1, qs_type, 'Wales' as qs_a1r, 'GB13000000' as qs_a1r_lc FROM gbr_localadmin_tmp WHERE qs_a1r_lc = 'W'" gbr_localadmin.shp gbr_localadmin_tmp.shp
	# Scotland is prefix null and -spat -196211 577762.31 625336.14 1319225
	ogr2ogr -append -f "ESRI Shapefile" -spat -9.2786562 55.1319922 4.431488 62.531353 -sql "SELECT qs_adm0_a3, qs_iso_cc, qs_adm0, qs_a0, qs_level, qs_source, qs_a1, 'Scotland' as qs_a1r, 'GB11000000' as qs_a1r_lc, 'Unitary Council' as qs_type FROM gbr_localadmin_tmp src WHERE qs_a1r_lc IS NULL" gbr_localadmin.shp gbr_localadmin_tmp.shp
	# add Northern Ireland
	ogr2ogr -f "Esri Shapefile" -append -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'GBR' as qs_adm0_a3, 'GB' as qs_iso_cc, 'United Kingdom' as qs_adm0, 'United Kingdom' as qs_a0, 'localadmin' as qs_level, 'EuroGlobalMap' as qs_source, 'ND' as qs_a0_lc, 'Northern Ireland' as qs_a1r, src.SHN1 as qs_a1r_lc, src.SHN4 as qs_a1_lc, namefile.NAMN as qs_a1, 'Unitary District' as qs_type FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN4 = namefile.SHN" gbr_localadmin.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/ND/PolbndA.shp
	rm -rf gbr_localadmin_tmp.*

# CANADA

can_localities.shp: can_adm1.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CAN' as qs_adm0_a3, 'Canada' as qs_adm0, 'locality' as qs_level, 'Canada Census' as qs_source, commoname1 as qs_loc, legalname1 as qs_loc_alt, nid as qs_loc_lc, localid as qs_loc_lc2, designatn as qs_type, type as qs_type2, datasetnam as qs_a1, namefile.qs_a1_lc as qs_a1_lc, 'CA' as qs_iso_cc, 'Canada' as qs_a0 FROM can_municipalities src LEFT JOIN '../nma/canada/provinces/cgb_lgc_canada_shp_en/can_adm1.dbf'.can_adm1 namefile ON src.datasetnam = namefile.qs_a1" can_localities.shp ../nma/canada/municipal_boundaries/merged/can_municipalities.shp
	
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'CAN' as qs_adm0_a3, 'Canada' as qs_adm0, 'locality' as qs_level, mun_name as qs_loc, f_code as qs_loc_lc, code as qs_type, 'BC Gov' as qs_source, 'CA' as qs_iso_cc, 'Canada' as qs_a0, 'BC' as qs_a1_lc, 'British Columbia' as qs_a1 FROM can_bc_TA_MUNICIP_polygon" can_localities.shp ../nma/canada/municipal_boundaries/merged/can_bc_TA_MUNICIP_polygon.shp
	
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'CAN' as qs_adm0_a3, 'Canada' as qs_adm0, 'locality' as qs_level, 'Canada Census' as qs_source, name1 as qs_loc, name2 as qs_loc_alt, nid as qs_loc_lc, jur1 as qs_a1_lc, namefile.qs_a1 as qs_a1, altype as qs_type, 'CA' as qs_iso_cc, 'Canada' as qs_a0 FROM AL_TA_CA_2_31_eng src LEFT JOIN '../nma/canada/provinces/cgb_lgc_canada_shp_en/can_adm1.dbf'.can_adm1 namefile ON src.jur1 = namefile.qs_a1_lc" can_localities.shp ../nma/canada/reserves/AL_TA_CA_2_31_eng.shp

can_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CAN' as qs_adm0_a3, 'Canada' as qs_adm0, 'adm1' as qs_level, 'Canada Census' as qs_source, namefile.qs_a1 as qs_a1, namefile.qs_a1_lc as qs_a1_lc, type_e as qs_type, 'CA' as qs_iso_cc, 'Canada' as qs_a0 FROM prov_ab_p_geo83_e src LEFT JOIN '../nma/canada/provinces/cgb_lgc_canada_shp_en/can_adm1.dbf'.can_adm1 namefile ON src.name = namefile.qs_a1_up" can_adm1.shp ../nma/canada/provinces/cgb_lgc_canada_shp_en/prov_ab_p_geo83_e.shp

can_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CAN' as qs_adm0_a3, 'Canada' as qs_adm0, 'adm0' as qs_level, 'Canada Census' as qs_source, name as qs_a0, type_e as qs_type, 'CA' as qs_iso_cc FROM can_ab_p_geo83_e" can_adm0.shp ../nma/canada/provinces/cgb_lgc_canada_shp_en/can_ab_p_geo83_e.shp


# BRAZIL

#-sql "SELECT 'BRA' as qs_adm0_a3, 'Brazil' as qs_adm0, 'adm2' as qs_level FROM 55mu2500gsr"

../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_clean.shp:
	# Orig in bad character encoding. Manually converted to UTF-8 using OpenOffice.
	# --config SHAPE_ENCODING "ISO-8859-15"
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_clean.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr.shp
	
bra_adm0.shp:
	# Trouble with dissolves and encodings!
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'BR' as qs_iso_cc, 'Brasil' as qs_a0, REGIão as qs_a1, geocodig_m as qs_a2_lc, uf as qs_a1_lc FROM 55mu2500gsr_clean" bra_adm2.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_clean.shp
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -nlt MULTIPOLYGON bra_adm0.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_adm0.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.adm0_a3 as qs_adm0_a3, src.admin as qs_adm0, 'adm0' as qs_level, src.iso_a2 as qs_iso_cc, src.admin as qs_a0, 'US State Department, with Natural Earth mods' as qs_source FROM us_state_department_countries_ne_hybrid src WHERE src.adm0_a3 in ('bra')" bra_adm0.shp ../us_state_department/final_data/us_state_department_countries_ne_hybrid.shp

	#dissolve-shapes.py -i bra_adm0.shp -o bra_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level


bra_adm1_eh.shp:
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT nome_munic as qs_a1, REGIão as qs_a1, geocodig_m as qs_a2_lc, uf as qs_a1_lc FROM 55mu2500gsr_clean" bra_adm2.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_clean.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -nlt MULTIPOLYGON bra_adm1.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_adm1.shp

	#dissolve-shapes.py -i bra_adm1.shp -o bra_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level

bra_adm2_eh.shp:
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" bra_adm2.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_clean2.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -nlt MULTIPOLYGON bra_adm2.shp ../nma/brazil/2nd_round/55mu2500gsr_admin_2/55mu2500gsr_adm2.shp
	

bra_adm1_src_data:
	mkdir -p raw_downloads/bra/adm1/
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ac.zip -O raw_downloads/bra/adm1/ac.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/al.zip -O raw_downloads/bra/adm1/al.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/am.zip -O raw_downloads/bra/adm1/am.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ap.zip -O raw_downloads/bra/adm1/ap.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ba.zip -O raw_downloads/bra/adm1/ba.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ce.zip -O raw_downloads/bra/adm1/ce.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/df.zip -O raw_downloads/bra/adm1/df.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/es.zip -O raw_downloads/bra/adm1/es.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/go.zip -O raw_downloads/bra/adm1/go.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ma.zip -O raw_downloads/bra/adm1/ma.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/mg.zip -O raw_downloads/bra/adm1/mg.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ms.zip -O raw_downloads/bra/adm1/ms.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/mt.zip -O raw_downloads/bra/adm1/mt.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/pa.zip -O raw_downloads/bra/adm1/pa.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/pb.zip -O raw_downloads/bra/adm1/pb.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/pe.zip -O raw_downloads/bra/adm1/pe.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/pi.zip -O raw_downloads/bra/adm1/pi.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/pr.zip -O raw_downloads/bra/adm1/pr.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/rj.zip -O raw_downloads/bra/adm1/rj.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/rn.zip -O raw_downloads/bra/adm1/rn.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/ro.zip -O raw_downloads/bra/adm1/ro.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/rr.zip -O raw_downloads/bra/adm1/rr.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/rs.zip -O raw_downloads/bra/adm1/rs.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/sc.zip -O raw_downloads/bra/adm1/sc.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/se.zip -O raw_downloads/bra/adm1/se.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/sp.zip -O raw_downloads/bra/adm1/sp.zip
	wget ftp://geoftp.ibge.gov.br/malhas_digitais/municipio_2010/to.zip -O raw_downloads/bra/adm1/to.zip
	unzip -o raw_downloads/bra/adm1/ac.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/al.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/am.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/ap.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/ba.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/ce.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/df.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/es.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/go.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/ma.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/mg.zip -d raw_downloads/bra/adm1/
	mkdir -p raw_downloads/bra/adm1/ms/
	unzip -o raw_downloads/bra/adm1/ms.zip -d raw_downloads/bra/adm1/ms/
	unzip -o raw_downloads/bra/adm1/mt.zip -d raw_downloads/bra/adm1/
	mkdir -p raw_downloads/bra/adm1/pa/
	unzip -o raw_downloads/bra/adm1/pa.zip -d raw_downloads/bra/adm1/pa/
	unzip -o raw_downloads/bra/adm1/pb.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/pe.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/pi.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/pr.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/rj.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/rn.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/ro.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/rr.zip -d raw_downloads/bra/adm1/
	mkdir -p raw_downloads/bra/adm1/rs/
	unzip -o raw_downloads/bra/adm1/rs.zip -d raw_downloads/bra/adm1/rs/
	mkdir -p raw_downloads/bra/adm1/sc/
	unzip -o raw_downloads/bra/adm1/sc.zip -d raw_downloads/bra/adm1/sc/
	unzip -o raw_downloads/bra/adm1/se.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/sp.zip -d raw_downloads/bra/adm1/
	unzip -o raw_downloads/bra/adm1/to.zip -d raw_downloads/bra/adm1/


bra_adm1.shp:	
	#  -sql "SELECT nm_municip as qs_loc, tipo as qs_type, cd_geocodm as qs_a1_lc1, nm_micro as qs_launame, nm_meso as qs_a2 FROM 12SEE250GC_SIR"
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="ISO-8859-15" --config SHAPE_ENCODING ISO-8859-15 -nlt MULTIPOLYGON -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ac/12UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/al/27UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/am/13UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ap/16UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ba/29UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ce/23UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/df/53UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/es/32UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/go/52UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ma/21UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/mg/31UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ms/50UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/mt/51UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/pa/15UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/pb/25UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/pe/26UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/pi/22UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/pr/41UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/rj/33UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/rn/24UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/ro/11UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/rr/14UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/rs/43UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/sc/42UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/se/28UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/sp/35UFE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm1.shp raw_downloads/bra/adm1/to/17UFE250GC_SIR.shp
	# now set the common attr
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="ISO-8859-15" --config SHAPE_ENCODING ISO-8859-15 -sql "SELECT 'BRA' as qs_adm0_a3, 'Brazil' as qs_adm0, 'adm1' as qs_level, 'BR' as qs_iso_cc, 'Brasil' as qs_a0, 'Brasil IBGE' as qs_source, cd_geocodu as qs_a1_lc, nm_estado as qs_a1, 'Estado' as qs_type FROM  bra_adm1" bra_adm1.shp bra_adm1.shp
	

#
# Other Brazil data comes from
#
# ftp://geoftp.ibge.gov.br/malhas_digitais/censo_2010/setores_censitarios/ac.zip

bra_adm2.shp:
	#  -sql "SELECT 'BRA' as qs_adm0_a3, 'Brazil' as qs_adm0, 'adm2' as qs_level, 'BR' as qs_iso_cc, 'Brasil' as qs_a0, 'Brasil IBGE' as qs_source, SUBSTR(cd_geocodm,0,2) as qs_a1_lc, cd_geocodm as qs_a2_lc, nm_municip as qs_a2 FROM 12MUE250GC_SIR"
	# --config SHAPE_ENCODING ISO-8859-15
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="ISO-8859-15" --config SHAPE_ENCODING ISO-8859-15 -nlt MULTIPOLYGON -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ac/12MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/al/27MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/am/13MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ap/16MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ba/29MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ce/23MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/df/53MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/es/32MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/go/52MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ma/21MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/mg/31MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ms/50MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/mt/51MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/pa/15MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/pb/25MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/pe/26MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/pi/22MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/pr/41MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/rj/33MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/rn/24MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/ro/11MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/rr/14MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/rs/43MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/sc/42MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/se/28MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/sp/35MUE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_adm2.shp ../nma/brazil/2nd_round/census_detailed/to/17MUE250GC_SIR.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="ISO-8859-15" --config SHAPE_ENCODING ISO-8859-15 -sql "SELECT 'BRA' as qs_adm0_a3, 'Brazil' as qs_adm0, 'adm2' as qs_level, 'BR' as qs_iso_cc, 'Brasil' as qs_a0, 'Brasil IBGE' as qs_source, cd_geocodm as qs_a2_lc, nm_municip as qs_a2, 'Municípios' as qs_type FROM  bra_adm2" bra_adm2.shp bra_adm2.shp

bra_localadmin.shp:	
	#  -sql "SELECT nm_municip as qs_loc, tipo as qs_type, cd_geocodm as qs_a1_lc1, nm_micro as qs_launame, nm_meso as qs_a2 FROM 12SEE250GC_SIR"
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -nlt MULTIPOLYGON -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ac/12DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/al/27DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/am/13DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ap/16DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ba/29DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ce/23DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/df/53DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/es/32DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/go/52DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ma/21DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/mg/31DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ms/50DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/mt/51DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/pa/15DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/pb/25DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/pe/26DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/pi/22DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/pr/41DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/rj/33DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/rn/24DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/ro/11DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/rr/14DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/rs/43DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/sc/42DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/se/28DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/sp/35DSE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_localadmin.shp ../nma/brazil/2nd_round/census_detailed/to/17DSE250GC_SIR.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="ISO-8859-15" --config SHAPE_ENCODING ISO-8859-15 -sql "SELECT 'BRA' as qs_adm0_a3, 'Brazil' as qs_adm0, 'localadmin' as qs_level, 'BR' as qs_iso_cc, 'Brasil' as qs_a0, 'Brasil IBGE' as qs_source, cd_geocodd as qs_la_lc, nm_distrit as qs_la, 'District' as qs_type FROM  bra_localadmin" bra_localadmin.shp bra_localadmin.shp
	
	
bra_district.shp:	
	#  -sql "SELECT nm_municip as qs_loc, tipo as qs_type, cd_geocodm as qs_a1_lc1, nm_micro as qs_launame, nm_meso as qs_a2 FROM 12SEE250GC_SIR"
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -nlt MULTIPOLYGON -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ac/12SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/al/27SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/am/13SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ap/16SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ba/29SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ce/23SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/df/53SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/es/32SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/go/52SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ma/21SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/mg/31SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ms/50SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/mt/51SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/pa/15SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/pb/25SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/pe/26SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/pi/22SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/pr/41SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/rj/33SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/rn/24SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/ro/11SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/rr/14SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/rs/43SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/sc/42SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/se/28SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/sp/35SEE250GC_SIR.shp
	ogr2ogr -append -f "ESRI Shapefile" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +no_defs" bra_district.shp ../nma/brazil/2nd_round/census_detailed/to/17SEE250GC_SIR.shp


bra_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'BRA' as qs_adm0_a3, 'Brazil' as qs_adm0, 'locality0' as qs_level, 'BR' as qs_iso_cc, 'Brasil' as qs_a0, 'Brasil IBGE' as qs_source, SUBSTR(cd_geocodm,0,2) as qs_a1_lc, qs_a1 as qs_a1, cd_geocodm as qs_a2_lc, nm_municip as qs_a2, qs_loc as qs_loc, qs_pop as qs_pop, qs_type as qs_type, qs_type2 as qs_type2 FROM  bra_district_combo_sel_buff_merge3_join3" bra_localities.shp ../nma/brazil/2nd_round/custom/bra_district_combo_sel_buff_merge3_join3.shp


# AUSTRALIA

aus_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'adm0' as qs_level, 'Australia Census' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0 FROM TR_2012_AUST" aus_adm0.shp ../nma/australia/1270055003_tr_2012_aust_shape/TR_2012_AUST.shp

	#dissolve-shapes.py -i aus_adm0.shp -o aus_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0
	
aus_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'adm1' as qs_level, 'Australia Census' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0, ste_name11 as qs_a1, ste_code11 as qs_a1_lc FROM TR_2012_AUST" aus_adm1.shp ../nma/australia/1270055003_tr_2012_aust_shape/TR_2012_AUST.shp

	#dissolve-shapes.py -i aus_adm1.shp -o aus_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a1,qs_a1_lc

aus_adm2.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'adm2' as qs_level, 'Australia Census' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0, lga_name12 as qs_a2, lga_code12 as qs_a2_lc, ste_code11 as qs_a1_lc, ste_name11 as qs_a1 FROM LGA_2012_AUST" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs EPSG:4283 aus_adm2.shp ../nma/australia/1270055003_lga_2012_aust_shape/LGA_2012_AUST.shp

	#dissolve-shapes.py -i aus_adm2.shp -o aus_adm2.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a1,qs_a1_lc,qs_a2,qs_a2_lc

aus_localadmin.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'localadmin' as qs_level, 'Australian Bureau Of Statistics' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0, SSC_NAME as qs_la, SSC_CODE as qs_la_lc, STATE_CODE as qs_a1_lc, STATE_NAME as qs_a1 FROM SSC_2011_AUST" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs EPSG:4019 aus_localadmin.shp ../nma/australia/2011_SSC_shape/SSC_2011_AUST.shp

aus_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'locality1' as qs_level, 'Australian Bureau Of Statistics: state suburbs file selection' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0, state_code as qs_a1_lc, state_name as qs_a1, ssc_name as qs_la, ssc_code as qs_la_lc, name as qs_loc FROM SSC_2011_AUST_custom WHERE locality IN (1,2,3)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs EPSG:4019 aus_localities.shp ../nma/australia/2011_SSC_shape/SSC_2011_AUST_custom.shp
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'locality1' as qs_level, 'Australian Bureau Of Statistics: state suburbs file with customization' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0, state_code as qs_a1_lc, state_name as qs_a1, ssc_name as qs_la, ssc_code as qs_la_lc, name as qs_loc FROM SSC_2011_AUST_custom_union_splits WHERE locality_1 IN (10)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs EPSG:4019 aus_localities.shp ../nma/australia/2011_SSC_shape/SSC_2011_AUST_custom_union_splits.shp
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'AUS' as qs_adm0_a3, 'Australia' as qs_adm0, 'locality1' as qs_level, 'Australian Bureau Of Statistics: urban areas and localities selection' as qs_source, 'AU' as qs_iso_cc, 'Australia' as qs_a0, name as qs_loc, ucl_code as qs_loc_lc, adm1_lc as qs_a1_lc, adm1 as qs_a1 FROM UCL06aAUST_region_custom_join WHERE locality IN (1)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs EPSG:4019 aus_localities.shp ../nma/australia/2006_UCL_AUST_ESRI_Shapefile/UCL06aAUST_region_custom_join.shp


# NETHERLANDS

# This needs to use the files that are in local grid now, they need to be reprojected.
#nld_adm1.shp:
#	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT naam as qs_a1 FROM 'admin-1_provinces'" nld_adm1.shp ../nma/netherlands/Dutch-admin/admin-1_provinces.shp
	
nld_localadmin.shp:
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT naam as qs_la FROM admin-2_municipalities" nld_localities.shp netherlands/Dutch-admin/admin-2_municipalities.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'NLD' as qs_adm0_a3, 'NL' as qs_iso_cc, 'Netherlands' as qs_adm0, 'Nederland' as qs_a0, 'localadmin' as qs_level, 'NLD Kadaster' as qs_source, gm_naam as qs_la, gm_code as qs_la_lc, 'Gemeenten' as qs_type FROM gem_2009_gen" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=sterea +lat_0=52.15616055555555 +lon_0=5.38763888888889 +k=0.9999079 +x_0=155000 +y_0=463000 +ellps=bessel +towgs84=565.417,50.3319,465.552,-0.398957,0.343988,-1.8774,4.0725 +units=m +no_defs" nld_localadmin.shp ../nma/netherlands/Dutch-admin/gem_2009_gen.shp

#NETHERLANDS EUROLGLOBALMAP

# Slightly better than NMA data
# Almost as good as the NMA open data (the NMA data includes exo areas, this doesn't).
# NMA has better coastline.

nld_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'NLD' as qs_adm0_a3, 'Netherlands' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" nld_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/NL/PolbndA.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1_lc as qs_a1_lc, namefile.DESN as qs_type FROM nld_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" nld_adm0.shp nld_adm0.shp


nld_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'NLD' as qs_adm0_a3, 'Netherlands' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM nld_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" nld_adm1.shp nld_adm0.shp	
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM nld_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" nld_adm1.shp nld_adm1.shp



# SPAIN

esp_localadmin.shp: esp_adm1.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ESP' as qs_adm0_a3, 'Spain' as qs_adm0, 'localadmin' as qs_level, 'Spain IGN' as qs_source, src.municipio as qs_la, SUBSTR(src.codine,0,2) as qs_a1_lc, src.codine as qs_la_lc, 'ES' as qs_iso_cc, 'Spain' as qs_a0 FROM Poligonos_municipios_ETRS89 src" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs" esp_localadmin.shp ../nma/spain/lineas_limite/ETRS89/Poligonos_municipios_ETRS89.shp
	# add adm1 names
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_adm0, qs_level, qs_source, qs_la, qs_a1_lc, namefile.qs_a1 as qs_a1, qs_la_lc, qs_iso_cc, qs_a0 FROM esp_localadmin src LEFT JOIN 'esp_adm1.dbf'.esp_adm1 namefile ON src.qs_a1_lc = namefile.qs_a1_lc" esp_localadmin.shp esp_localadmin.shp	


esp_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ESP' as qs_adm0_a3, 'Spain' as qs_adm0, 'adm1' as qs_level, 'Spain IGN' as qs_source, nombre as qs_a1, codine as qs_a1_lc, 'ES' as qs_iso_cc, 'Spain' as qs_a0 FROM Poligonos_Provincias_ETRS89" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs" esp_adm1.shp ../nma/spain/lineas_limite/ETRS89/Poligonos_Provincias_ETRS89.shp

esp_adm1_region.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ESP' as qs_adm0_a3, 'Spain' as qs_adm0, 'adm1_region' as qs_level, 'Spain IGN' as qs_source, nombre as qs_a1r, 'Comunidad Autónoma' as qs_type, cod_ccaa as qs_a1r_lc, 'ES' as qs_iso_cc, 'Spain' as qs_a0 FROM Poligonos_CCAA_ETRS89" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs" esp_adm1_region.shp ../nma/spain/lineas_limite/ETRS89/Poligonos_CCAA_ETRS89.shp

# SPAIN EUROGLOBALMAP
# Almost as good as the NMA open data (the NMA data includes exo areas, this doesn't).
# NMA has better coastline.

esp_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('ES')" esp_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/ES/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'ESP' as qs_adm0_a3, 'Spain' as qs_adm0, 'adm0' as qs_level, 'ES' as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source, 'Spain' as qs_a0 FROM esp_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" esp_adm0.shp esp_adm0_tmp.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, namefile.DESN as qs_type FROM esp_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" esp_adm0.shp esp_adm0.shp
	rm esp_adm0_tmp.*

#esp_adm1_region.shp:
#	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM esp_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" esp_adm1_region.shp esp_adm0.shp

#esp_adm1.shp:
#	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM esp_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" esp_adm1.shp esp_adm1_region.shp


#Gibraltar

gib_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('GI')" gib_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/ES/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'GIB' as qs_adm0_a3, 'Gibraltar' as qs_adm0, 'adm0' as qs_level, 'GI' as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source, 'Gibraltar' as qs_a0 FROM gib_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" gib_adm0.shp gib_adm0_tmp.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, namefile.DESN as qs_type FROM gib_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" gib_adm0.shp gib_adm0.shp
	rm gib_adm0_tmp.*

gib_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_adm0, 'adm1' as qs_level, qs_source, qs_iso_cc, qs_a0, qs_a0_alt, qs_a0_lc FROM gib_adm0" gib_adm1.shp gib_adm0.shp 

# ITALY

ita_localadmin.shp: \
	ita_adm1.shp \
	ita_adm1_region.shp
	
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ITA' as qs_adm0_a3, 'Italy' as qs_adm0, 'localadmin' as qs_level, 'Italy IGN' as qs_source, 'IT' as qs_iso_cc, 'Italy' as qs_a0, src.nome_com as qs_la, src.nome_ted as qs_la_alt, src.pro_com as qs_la_lc, namefile.qs_a1 as qs_a1, src.cod_pro as qs_a1_lc, namefile2.qs_a1r as qs_a1r, src.cod_reg as qs_a1r_lc FROM com2011 src LEFT JOIN 'ita_adm1.dbf'.ita_adm1 namefile ON src.cod_pro = namefile.qs_a1_lc LEFT JOIN 'ita_adm1_region.dbf'.ita_adm1_region namefile2 ON src.cod_reg = namefile2.qs_a1r_lc" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=32 +ellps=intl +towgs84=-115.854,-99.0583,-152.462,0,0,0,0 +units=m +no_defs" ita_localadmin.shp ../nma/italy/com2011/com2011.shp

ita_adm1.shp: ita_adm1_region.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ITA' as qs_adm0_a3, 'Italy' as qs_adm0, 'adm1' as qs_level, 'Italy IGN' as qs_source, 'IT' as qs_iso_cc, 'Italy' as qs_a0, src.nome_pro as qs_a1, src.cod_pro as qs_a1_lc, src.cod_reg as qs_a1r_lc, namefile.qs_a1r as qs_a1r FROM prov2011 src LEFT JOIN 'ita_adm1_region.dbf'.ita_adm1_region namefile ON src.cod_reg = namefile.qs_a1r_lc" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=32 +ellps=intl +towgs84=-115.854,-99.0583,-152.462,0,0,0,0 +units=m +no_defs" ita_adm1.shp ../nma/italy/prov2011/prov2011.shp

ita_adm1_region.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ITA' as qs_adm0_a3, 'Italy' as qs_adm0, 'adm1_region' as qs_level, 'Italy IGN' as qs_source, 'IT' as qs_iso_cc, 'Italy' as qs_a0, nome_reg as qs_a1r, cod_reg as qs_a1r_lc, 'Regioni' as qs_type FROM reg2011" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=32 +ellps=intl +towgs84=-115.854,-99.0583,-152.462,0,0,0,0 +units=m +no_defs" ita_adm1_region.shp ../nma/italy/reg2011/reg2011.shp

# ITALY EUROGLOBALMAP
# Almost as good as the NMA open data (the NMA data includes exo areas, this doesn't).
# NMA has better coastline.

ita_adm0.shp:
	rm -f ita_adm0_tmp.*
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('IT')" ita_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/IT/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'ITA' as qs_adm0_a3, 'Italy' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM ita_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" ita_adm0.shp ita_adm0_tmp.shp
	rm -f ita_adm0_tmp.*

#ita_adm1_region.shp:
#	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM ita_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" ita_adm1_region.shp ita_adm0.shp

#ita_adm1.shp:
#	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM ita_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" ita_adm1.shp ita_adm1_region.shp


#SAN MARINO

smr_adm0.shp:
	rm -f smr_adm0_tmp.*
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('SM')" smr_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/IT/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'SMR' as qs_adm0_a3, 'San Marino' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM smr_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" smr_adm0.shp smr_adm0_tmp.shp
	rm -f smr_adm0_tmp.*
	
#VATICAN
	
vat_adm0.shp:
	rm -f vat_adm0_tmp.*
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('VA')" vat_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/IT/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'VAT' as qs_adm0_a3, 'Vatican' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM vat_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" vat_adm0.shp vat_adm0_tmp.shp
	rm -f vat_adm0_tmp.*

vat_adm1.shp: 
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.adm0_a3 as qs_adm0_a3, src.admin as qs_adm0, 'adm1' as qs_level, src.iso_a2 as qs_iso_cc, src.admin as qs_a0, 'US State Department, with Natural Earth mods' as qs_source FROM us_state_department_countries_ne_hybrid src WHERE src.adm0_a3 in ('vat')" vat_adm1.shp ../us_state_department/final_data/us_state_department_countries_ne_hybrid.shp

# FRANCE

fra_localadmin.shp:
	#metropolitan france
	# --config SHAPE_ENCODING ISO-8859-15 didn't work so manually mod'd to UTF-8
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0, 'localadmin' as qs_level, 'France IGN' as qs_source, nom_comm as qs_la, insee_com as qs_la_lc, code_comm as qs_la_lc2, statut as qs_type, code_arr as qs_a2r_lc, code_cant as qs_a2_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r FROM COMMUNE" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=lcc +lat_1=44 +lat_2=49 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +units=m +no_defs" fra_localadmin.shp ../nma/france/GEOFLA_1-1_SHP_LAMB93_FR-ED111/COMMUNES/COMMUNE.SHP

	# mayotte
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0,  'localadmin' as qs_level, 'France IGN' as qs_source, nom_comm as qs_la, insee_com as qs_la_lc, code_comm as qs_la_lc2, statut as qs_type, code_arr as qs_a2r_lc, code_cant as qs_a2_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r FROM COMMUNE" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=38 +south +ellps=GRS80 +units=m +no_defs" fra_localadmin.shp ../nma/france/GEOFLA_1-1_SHP_RGM04UTM38S_YT-ED111/COMMUNES/COMMUNE.SHP

	# reunion
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0,  'localadmin' as qs_level, 'France IGN' as qs_source, nom_comm as qs_la, insee_com as qs_la_lc, code_comm as qs_la_lc2, statut as qs_type, code_arr as qs_a2r_lc, code_cant as qs_a2_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r FROM COMMUNE" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=40 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs" fra_localadmin.shp ../nma/france/GEOFLA_1-1_SHP_RGR92UTM40S_RE-ED111/COMMUNES/COMMUNE.SHP
	
	# Guadeloupe
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0,  'localadmin' as qs_level, 'France IGN' as qs_source, nom_comm as qs_la, insee_com as qs_la_lc, code_comm as qs_la_lc2, statut as qs_type, code_arr as qs_a2r_lc, code_cant as qs_a2_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r FROM COMMUNE" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=20 +datum=WGS84 +units=m +no_defs" fra_localadmin.shp ../nma/france/GEOFLA_1-1_SHP_UTM20W84_GP-ED111/COMMUNES/COMMUNE.SHP
	
	# Martinique
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0,  'localadmin' as qs_level, 'France IGN' as qs_source, nom_comm as qs_la, insee_com as qs_la_lc, code_comm as qs_la_lc2, statut as qs_type, code_arr as qs_a2r_lc, code_cant as qs_a2_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r FROM COMMUNE" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=20 +datum=WGS84 +units=m +no_defs" fra_localadmin.shp ../nma/france/GEOFLA_1-1_SHP_UTM20W84_MQ-ED111/COMMUNES/COMMUNE.SHP
	
	# (french) Guyane
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0,  'localadmin' as qs_level, 'France IGN' as qs_source, nom_comm as qs_la, insee_com as qs_la_lc, code_comm as qs_la_lc2, statut as qs_type, code_arr as qs_a2r_lc, code_cant as qs_a2_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r FROM COMMUNE" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=utm +zone=22 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs" fra_localadmin.shp ../nma/france/GEOFLA_1-1_SHP_UTM22RGFG95_GF-ED111/COMMUNES/COMMUNE.SHP


fra_adm2_region.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -lco ENCODING="UTF-8" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0, 'adm2_region' as qs_level, 'France IGN' as qs_source, nom_chf as qs_a2r, code_arr as qs_a2r_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r, 'Arrondissement' as qs_type FROM ARRONDISSEMENT" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=lcc +lat_1=44 +lat_2=49 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +units=m +no_defs" fra_adm2_region.shp ../nma/france/GEOFLA_1-1_SHP_LAMB93_FR-ED111/ARRONDISSEMENTS/ARRONDISSEMENT.SHP

fra_adm2.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" --config SHAPE_ENCODING ISO-8859-15 -lco ENCODING="UTF-8" -sql "SELECT 'FRA' as qs_adm0_a3, 'FR' as qs_iso_cc, 'France' as qs_adm0, 'France' as qs_a0, 'adm2' as qs_level, 'France IGN' as qs_source, nom_chf as qs_a2, code_cant as qs_a2_lc, code_chf as qs_a2_lc2, code_arr as qs_a2r_lc, code_dept as qs_a1_lc, code_reg as qs_a1r_lc, nom_dept as qs_a1, nom_region as qs_a1r, 'Canton' as qs_type FROM CANTON" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=lcc +lat_1=44 +lat_2=49 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +units=m +no_defs" fra_adm2.shp ../nma/france/GEOFLA_1-1_SHP_LAMB93_FR-ED111/CANTONS/CANTON.SHP

#fra_adm1.shp:
#	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT nom_dept as qs_a1, code_dept as qs_a1_lc, nom_chf as qs_a1_alt, code_chf as qs_a1_lc2, code_reg as qs_a1r_lc, nom_region as qs_a1r FROM DEPARTEMENT" -t_srs "+proj=longlat +datum=WGS84 +no_defs"  -s_srs "+proj=lcc +lat_1=44 +lat_2=49 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +units=m +no_defs" fra_adm1.shp ../nma/france/GEOFLA_1-1_SHP_LAMB93_FR-ED111/DEPARTEMENTS/DEPARTEMENT.SHP

# FRANCE EUROGLOBALMAP
# Better than the NMA open data.

fra_adm0.shp:
	rm -f fra_adm0_tmp.*
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('FR')" fra_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/FR/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'FRA' as qs_adm0_a3, 'France' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM fra_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" fra_adm0.shp fra_adm0_tmp.shp
	rm -f fra_adm0_tmp.*
	

fra_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'FRA' as qs_adm0_a3, 'France' as qs_adm0, 'adm1_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM fra_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" fra_adm1_region.shp fra_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, namefile.DESN as qs_type FROM fra_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" fra_adm1_region.shp fra_adm1_region.shp
	
fra_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'FRA' as qs_adm0_a3, 'France' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM fra_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" fra_adm1.shp fra_adm1_region.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM fra_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" fra_adm1.shp fra_adm1.shp

# MONACO

mco_adm0.shp:
	rm -f mco_adm0_tmp.*
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM PolbndA src WHERE src.ICC IN ('MC')" mco_adm0_tmp.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/FR/PolbndA.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'MCO' as qs_adm0_a3, 'Monaco' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM mco_adm0_tmp src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" mco_adm0.shp mco_adm0_tmp.shp
	rm -f mco_adm0_tmp.*

mco_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'MCO' as qs_adm0_a3, 'Monaco' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM mco_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" mco_adm1.shp mco_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM mco_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" mco_adm1.shp mco_adm1.shp

	
# RUSSIA

rus_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" --config SHAPE_ENCODING UTF-8 -lco ENCODING="UTF-8" -sql "SELECT 'RUS' as qs_adm0_a3, 'Russia' as qs_adm0, 'localadmin' as qs_level, 'Unknown' as qs_source, 'RU' as qs_iso_cc, 'Российская Федерация' as qs_a0, nam as qs_loc, name as qs_loc_alt, code as qs_a1_lc, type as qs_type, subject as qs_a1, rayon as qs_a2 FROM 'pop-built-up-a-gislab'" rus_localities.shp ../nma/russia/population-gislab/pop-built-up-a-gislab.shp

rus_adm1.shp:
	# The src had irreconcilable Windows-1251 encoding that OGR refuses to translate.
	# Solution: open in OpenOffice and save as OO format (Unicode native), then save as as DBF with explicate UTF-8 encoding.
	#--config SHAPE_ENCODING "Windows-1251"
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'RUS' as qs_adm0_a3, 'Russia' as qs_adm0, 'adm1' as qs_level, 'Unknown' as qs_source, 'RU' as qs_iso_cc, 'Российская Федерация' as qs_a0, region as qs_a1, universal as qs_a1_alt FROM regions2010_wgs" rus_adm1.shp ../nma/russia/regions2010_wgs_shp/regions2010_wgs.shp

rus_adm0.shp:
	# The src had irreconcilable Windows-1251 encoding that OGR refuses to translate.
	# Solution: open in OpenOffice and save as OO format (Unicode native), then save as as DBF with explicate UTF-8 encoding.
	#--config SHAPE_ENCODING "Windows-1251"
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'RUS' as qs_adm0_a3, 'Russia' as qs_adm0, 'adm0' as qs_level, 'Unknown' as qs_source, 'RU' as qs_iso_cc, 'Российская Федерация' as qs_a0 FROM regions2010_wgs" rus_adm0.shp ../nma/russia/regions2010_wgs_shp/regions2010_wgs.shp

	#dissolve-shapes.py -i rus_adm0.shp -o rus_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0


# MEXICO

mex_localities.shp: mex_adm2.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'MEX' as qs_adm0_a3, 'Mexico' as qs_adm0, 'locality' as qs_level, 'Mexico IGN' as qs_source, 'MX' as qs_iso_cc, 'Mexico' as qs_a0, nom_loc as qs_loc, cve_loc as qs_a1_lc, cve_ent + cve_mun as qs_a2_lc, cve_mun as qs_a2_lc2, cve_ent as qs_a1_lc FROM POLIGONOS_URBANOS src" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=lcc +lat_1=17.5 +lat_2=29.5 +lat_0=12 +lon_0=-102 +x_0=2500000 +y_0=0 +ellps=GRS80 +units=m +no_defs" mex_localities.shp ../nma/mexico/LOCURBANAS50/POLIGONOS_URBANOS.shp
	# add adm1 and adm2 names
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_adm0, qs_level, qs_source, qs_iso_cc, qs_a0, qs_loc, qs_a1_lc, qs_a2_lc, qs_a2_lc2, qs_a1_lc, namefile.qs_a1 as qs_a1, namefile.qs_a2 as qs_a2 FROM mex_localities src LEFT JOIN 'mex_adm2.dbf'.mex_adm2 namefile ON src.qs_a2_lc = namefile.qs_a2_lc" mex_localities.shp mex_localities.shp

mex_adm2.shp: mex_adm1.shp
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'MEX' as qs_adm0_a3, 'Mexico' as qs_adm0, 'adm2' as qs_level, 'Mexico IGN' as qs_source, 'MX' as qs_iso_cc, 'Mexico' as qs_a0, src.nom_mun as qs_a2, src.cve_ent + src.cve_mun as qs_a2_lc, src.cve_mun as qs_a2_lc2, src.cve_ent as qs_a1_lc, namefile.qs_a1 as qs_a1 FROM MUNICIPIOS src LEFT JOIN 'mex_adm1.dbf'.mex_adm1 namefile ON src.cve_ent = namefile.qs_a1_lc" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=lcc +lat_1=17.5 +lat_2=29.5 +lat_0=12 +lon_0=-102 +x_0=2500000 +y_0=0 +ellps=GRS80 +units=m +no_defs" mex_adm2.shp ../nma/mexico/MUNICIPIOS50/MUNICIPIOS.shp

mex_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'MEX' as qs_adm0_a3, 'Mexico' as qs_adm0, 'adm1' as qs_level, 'Mexico IGN' as qs_source, 'MX' as qs_iso_cc, 'Mexico' as qs_a0, nom_ent as qs_a1, cve_ent as qs_a1_lc FROM ESTADOS" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=lcc +lat_1=17.5 +lat_2=29.5 +lat_0=12 +lon_0=-102 +x_0=2500000 +y_0=0 +ellps=GRS80 +units=m +no_defs" mex_adm1.shp ../nma/mexico/ESTADOS50/ESTADOS.shp

mex_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'MEX' as qs_adm0_a3, 'Mexico' as qs_adm0, 'adm0' as qs_level, 'Mexico IGN' as qs_source, 'MX' as qs_iso_cc, 'Mexico' as qs_a0 FROM ESTADOS" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=lcc +lat_1=17.5 +lat_2=29.5 +lat_0=12 +lon_0=-102 +x_0=2500000 +y_0=0 +ellps=GRS80 +units=m +no_defs" mex_adm0.shp ../nma/mexico/ESTADOS50/ESTADOS.shp

	#dissolve-shapes.py -i mex_adm0.shp -o mex_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0


# NEW ZEALAND

nzl_localities.shp:
	# New Zealand north and south islands
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'NZL' as qs_adm0_a3, 'New Zealand' as qs_adm0, 'NZ' as qs_iso_cc, 'New Zealand' as qs_a0, 'locality' as qs_level, 'Unknown' as qs_source, name as qs_loc FROM 'nz-residential-areas'" nzl_localities.shp ../nma/new_zealand/kx-nz-residential-areas-SHP/nz-residential-areas.shp
	
nzl_adm2.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'NZL' as qs_adm0_a3, 'New Zealand' as qs_adm0, 'adm2' as qs_level, 'New Zealand LINZ' as qs_source, 'NZ' as qs_iso_cc, 'New Zealand' as qs_a0, name as qs_a2, ta12 as qs_a2_lc FROM 'nz-territorial-authoritie'" nzl_adm2.shp ../nma/new_zealand/kx-nz-territorial-authorities-2012-yearly-pattern-clipped-SHP/nz-territorial-authoritie.shp

nzl_adm1.shp:
	# New Zealand north and south islands
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'NZL' as qs_adm0_a3, 'New Zealand' as qs_adm0, 'adm1' as qs_level, 'New Zealand LINZ' as qs_source, 'NZ' as qs_iso_cc, 'New Zealand' as qs_a0, name as qs_a1, regc12 as qs_a1_lc FROM 'nz-regional-councils-2012'" nzl_adm1.shp ../nma/new_zealand/kx-nz-regional-councils-2012-yearly-pattern-SHP/nz-regional-councils-2012.shp
	
	# chatham Islands
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'NZL' as qs_adm0_a3, 'New Zealand' as qs_adm0, 'adm1' as qs_level, 'New Zealand LINZ' as qs_source, 'NZ' as qs_iso_cc, 'New Zealand' as qs_a0, 'Chatham Islands' as qs_a1, regc12 as qs_a1_lc, mb12 as qs_a1_lc2 FROM 'nz-regional-councils-chat'" nzl_adm1.shp ../nma/new_zealand/kx-nz-regional-councils-chatham-islands-2012-yearly-pattern-SHP/nz-regional-councils-chat.shp

nzl_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'NZL' as qs_adm0_a3, 'New Zealand' as qs_adm0, 'adm0' as qs_level, 'New Zealand LINZ' as qs_source, 'NZ' as qs_iso_cc, 'New Zealand' as qs_a0 FROM 'nz-territorial-authoritie'" nzl_adm0.shp ../nma/new_zealand/kx-nz-territorial-authorities-2012-yearly-pattern-clipped-SHP/nz-territorial-authoritie.shp

	#dissolve-shapes.py -i nzl_adm0.shp -o nzl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0


#SWITZERLAND

# NOTE: The Swiss open data is better than the EuroGlobalMap, skip adm1 and adm0 from there, dissolve instead from the localadmin here:

che_localadmin.shp:
	# first the cantons with adm-2 divisions
	# We need to do this explicately as this data is slightly out of date (2 have adm2 marked, but since 2005 and 2007 they don't function)
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'localadmin' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, kantonsnum as qs_a1_lc, namefile.name as qs_a2, bezirksnum as qs_a2_lc, 'Commune' as qs_type, name as qs_la, bfs_nummer as qs_la_lc2, shn as qs_la_lc FROM TLM_HOHEITSGEBIET src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_BEZIRKSNAME.dbf'.TLM_BEZIRKSNAME namefile ON bezirksnum = namefile.NUMMER WHERE ICC = 'CH' and kantonsnum IN (1,2,5,10,13,17,18,19,20,21,22,23,24,26)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_localadmin_temp.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	#add in Appenzell Innerrhoden canton (it has weird adm2 coding, use bfs_nummer instead of bezirksnum)
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'localadmin' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, kantonsnum as qs_a1_lc, namefile.name as qs_a2, bezirksnum as qs_a2_lc, 'Bezirke' as qs_type, NULL as qs_la, bfs_nummer as qs_la_lc2, shn as qs_la_lc FROM TLM_HOHEITSGEBIET src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/swiss_names.dbf'.swiss_names namefile ON bfs_nummer = namefile.unique WHERE ICC = 'CH' and kantonsnum IN (16)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_localadmin_temp.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	#add in the unitary cantons (effectively nulling their adm2 data if present)
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'localadmin' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, kantonsnum as qs_a1_lc, bezirksnum as qs_a2_lc, 'Commune' as qs_type, name as qs_la, bfs_nummer as qs_la_lc, shn as qs_la_lc2 FROM TLM_HOHEITSGEBIET WHERE ICC = 'CH' and kantonsnum IN (3,4,6,7,8,9,11,12,14,15,25)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_localadmin_temp.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	# Now add in the adm1 names
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_adm0, qs_level, qs_source, qs_iso_cc, qs_a0, qs_a1_lc, qs_a2, qs_a2_lc, qs_type, qs_la, qs_la_lc, qs_la_lc2, namefile.name as qs_a1 FROM che_localadmin_temp src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_KANTONSNAME.dbf'.TLM_KANTONSNAME namefile ON qs_a1_lc = namefile.NUMMER"  che_localadmin.shp che_localadmin_temp.shp
	rm che_localadmin_temp.*




# Berzirk (Berzirkes)
che_adm2.shp:
	# first the cantons with adm-2 divisions
	# We need to do this explicately as this data is slightly out of date (2 have adm2 marked, but since 2005 and 2007 they don't function)
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'adm2' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, kantonsnum as qs_a1_lc, bezirksnum as qs_a2_lc, 'Bezirke' as qs_type, namefile.name as qs_a2 FROM TLM_HOHEITSGEBIET src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_BEZIRKSNAME.dbf'.TLM_BEZIRKSNAME namefile ON src.bezirksnum = namefile.NUMMER WHERE ICC = 'CH' and kantonsnum IN (1,2,5,10,13,17,18,19,20,21,22,23,24,26)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_adm2_temp.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	#add in Appenzell Innerrhoden canton (it has weird adm2 coding, use bfs_nummer instead of bezirksnum)
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'adm2' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, kantonsnum as qs_a1_lc, bfs_nummer as qs_a2_lc, 'Bezirke' as qs_type, namefile.name as qs_a2 FROM TLM_HOHEITSGEBIET src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/swiss_names.dbf'.swiss_names namefile ON src.bfs_nummer = namefile.unique WHERE ICC = 'CH' and kantonsnum IN (16)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_adm2_temp.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	#add in the unitary cantons (effectively nulling their adm2 data if present)
	ogr2ogr -append -f "ESRI Shapefile" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'adm2' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, kantonsnum as qs_a1_lc, 'bezirkefreie Canton' as qs_type FROM TLM_HOHEITSGEBIET WHERE ICC = 'CH' and kantonsnum IN (3,4,6,7,8,9,11,12,14,15,25)" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_adm2_temp.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	# Now add in the adm2 names
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_adm0, qs_level, qs_source, qs_iso_cc, qs_a0, qs_a1_lc, qs_a2_lc, qs_type, namefile.name as qs_a2 FROM che_adm2_temp src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/swiss_names.dbf'.swiss_names namefile ON qs_a2_lc = namefile.unique"  che_adm2_temp2.shp che_adm2_temp.shp
	# Now add in the adm1 names
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT qs_adm0_a3, qs_adm0, qs_level, qs_source, qs_iso_cc, qs_a0, qs_a1_lc, qs_a2, qs_a2_lc, qs_type, namefile.name as qs_a1 FROM che_adm2_temp src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_KANTONSNAME.dbf'.TLM_KANTONSNAME namefile ON qs_a1_lc = namefile.NUMMER"  che_adm2.shp che_adm2_temp.shp
	rm -rf che_adm2_temp.*
	rm -rf che_adm2_temp2.*
		
che_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'adm1' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, 'Canton' as qs_type, kantonsnum as qs_a1_lc, namefile.UUID as qs_a1 FROM TLM_HOHEITSGEBIET src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_KANTONSNAME.dbf'.TLM_KANTONSNAME namefile ON src.kantonsnum = namefile.UUID WHERE ICC = 'CH'" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_adm1.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp	
	# Old method
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'adm1' as qs_level, 'SwissTopo' as qs_source, 'CH' as qs_iso_cc, 'Switzerland' as qs_a0, 'Canton' as qs_type, kantonsnum as qs_a1_lc, namefile.name as qs_a1 FROM TLM_HOHEITSGEBIET src LEFT JOIN '../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/swiss_names.dbf'.swiss_names namefile ON src.kantonsnum = namefile.unique WHERE ICC = 'CH'" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_adm1.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp	

	#dissolve-shapes.py -i che_adm1.shp -o che_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a1_lc

che_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'CHE' as qs_adm0_a3, 'Switzerland' as qs_adm0, 'adm0' as qs_level, 'CH' as qs_iso_cc, 'SwissTopo' as qs_source, 'Switzerland' as qs_a0 FROM TLM_HOHEITSGEBIET WHERE ICC = 'CH'" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" che_adm0.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp


#LIECHTENSTEIN

lie_localadmin.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'LIE' as qs_adm0_a3, 'Liechtenstein' as qs_adm0, 'localadmin' as qs_level, 'SwissTopo' as qs_source, name as qs_la, 'LI' as qs_iso_cc, 'Liechtenstein' as qs_a0, bfs_nummer as qs_la_lc, shn as qs_la_lc2, kantonsnum as qs_a1_lc FROM TLM_HOHEITSGEBIET WHERE ICC = 'LI'" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" lie_localadmin.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp
	
lie_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'LIE' as qs_adm0_a3, 'Liechtenstein' as qs_adm0, 'adm1' as qs_level, 'SwissTopo' as qs_source, 'LI' as qs_iso_cc, 'Liechtenstein' as qs_a0, kantonsnum as qs_a1_lc FROM TLM_HOHEITSGEBIET WHERE ICC = 'LI'" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" lie_adm1.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp


lie_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'LIE' as qs_adm0_a3, 'Liechtenstein' as qs_adm0, 'adm0' as qs_level, 'LI' as qs_iso_cc, 'SwissTopo' as qs_source, 'Liechtenstein' as qs_a0 FROM TLM_HOHEITSGEBIET WHERE ICC = 'LI'" -t_srs "+proj=longlat +datum=WGS84 +no_defs" -s_srs "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs" lie_adm0.shp ../nma/switzerland/swissBOUNDARIES3D080312/Boundaries_2012/swissBOUNDARIES3D/SHAPEFILE_LV95_LN02/TLM_HOHEITSGEBIET.shp

# EUROPEAN UNION

eu_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_a0 as qs_adm0, 'locality' as qs_level, 'Custom EuroGlobalMap + UMZ Urban Polygons + Geonames + GeoPlanet' as qs_source, src.qs_name as qs_loc, src.qs_name2 as qs_loc_alt, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2r as qs_a2r, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_la_lc as qs_la_lc, src.qs_la as qs_la, src.qs_a0_alt as qs_a0_alt, src.qs_a1_alt as qs_a1_alt, src.qs_a2_alt as qs_a2_alt, src.qs_type as qs_type, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.woe_id as qs_woe_id, src.gn_id as qs_gn_id, src.qs_pop as qs_pop FROM umz_combo204_admins src" eu_localities.shp ../europe_localities/umz_combo204_admins.shp
	# WHERE qs_iso_cc NOT IN ('gb','tr')
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'EE' as qs_adm0_a3, 'Europe' as qs_adm0, 'locality' as qs_level, 'EuroGlobalMap' as qs_source, icc as qs_iso_cc, nama1 as qs_loc, namn1 as qs_loc_alt, gfid as qs_loc_lc, ppl as qs_pop FROM BuiltupA" eu_localities.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/BuiltupA.shp
	
	# This is the separate urban areas that are funky
	#ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'EE' as qs_adm0_a3, 'Europe' as qs_adm0, 'locality' as qs_level, comm_name as qs_loc, umz06_id as qs_a1_lc, comm_id as qs_a1_lc1, cntr_code as qs_a0_lc, nuts_code as qs_nuts FROM UMZ2006_geo_names" eu_localities.shp ../nma/00_eu_nuts/UMZ2006_f3v0_vector/UMZ2006_geo_names.shp


# INDONESIA

idn_adm2.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'IDN' as qs_adm0_a3, 'Indonesia' as qs_adm0, 'adm2' as qs_level, 'GlobalMap' as qs_source, 'ID' as qs_iso_cc, 'Indonesia' as qs_a0, laa as qs_a2, nam as qs_a1, f_code_des as qs_type, coc as qs_a0_lc FROM polbnda" idn_adm2.shp ../global_map/a_core_priority/indonesia/polbnda.shp
	
	#dissolve-shapes.py -i idn_adm2.shp -o idn_adm2_test.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a1,qs_a0_lc,qs_a1,qs_a2,qs_type

idn_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'IDN' as qs_adm0_a3, 'Indonesia' as qs_adm0, 'adm1' as qs_level, 'GlobalMap' as qs_source, 'ID' as qs_iso_cc, 'Indonesia' as qs_a0, nam as qs_a1, coc as qs_a0_lc FROM polbnda" idn_adm1.shp ../global_map/a_core_priority/indonesia/polbnda.shp
	
	#dissolve-shapes.py -i idn_adm1.shp -o idn_adm2_test.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a0_lc,qs_a1

idn_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'IDN' as qs_adm0_a3, 'Indonesia' as qs_adm0, 'adm0' as qs_level, 'GlobalMap' as qs_source, 'ID' as qs_iso_cc, 'Indonesia' as qs_a0 FROM polbnda" idn_adm0.shp ../global_map/a_core_priority/indonesia/polbnda.shp

	#dissolve-shapes.py -i idn_adm0.shp -o idn_adm0_test.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a0_lc


# CHILE

chl_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -spat -118.184399 -14.007111 -60.024335  -58.652802 -sql "SELECT 'CHL' as qs_adm0_a3, 'Chile' as qs_adm0, 'locality' as qs_level, 'GlobalMap' as qs_source, 'CL' as qs_iso_cc, 'Chile' as qs_a0, nam as qs_loc, f_code_des as qs_type, soc as qs_a0_lc FROM builtupa" chl_localities.shp ../global_map/b_core_priority/chl/builtupa.shp
	
chl_adm2.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -spat -118.184399 -14.007111 -60.024335  -58.652802 -sql "SELECT 'CHL' as qs_adm0_a3, 'Chile' as qs_adm0, 'adm2' as qs_level, 'GlobalMap' as qs_source, 'CL' as qs_iso_cc, 'Chile' as qs_a0, laa as qs_a2, nam as qs_a1, f_code_des as qs_type FROM polbnda" chl_adm2.shp ../global_map/b_core_priority/chl/polbnda.shp
	
chl_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -spat -118.184399 -14.007111 -60.024335  -58.652802 -sql "SELECT 'CHL' as qs_adm0_a3, 'Chile' as qs_adm0, 'adm1' as qs_level, 'GlobalMap' as qs_source, 'CL' as qs_iso_cc, 'Chile' as qs_a0, nam as qs_a1, coc as qs_a0_lc  FROM polbnda" chl_adm1.shp ../global_map/b_core_priority/chl/polbnda.shp

	#dissolve-shapes.py -i chl_adm1.shp -o chl_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a1,qs_a0_lc


chl_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -spat -118.184399 -14.007111 -60.024335  -58.652802 -sql "SELECT 'CHL' as qs_adm0_a3, 'Chile' as qs_adm0, 'adm0' as qs_level, 'GlobalMap' as qs_source, 'CL' as qs_iso_cc, 'Chile' as qs_a0, coc as qs_a0_lc FROM polbnda" chl_adm0.shp ../global_map/b_core_priority/chl/polbnda.shp
	
	#dissolve-shapes.py -i chl_adm0.shp -o chl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a0_lc


# PALESTINE

pse_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PSE' as qs_adm0_a3, 'Palestine' as qs_adm0, 'locality' as qs_level, 'GlobalMap' as qs_source, 'PS' as qs_iso_cc, 'Palestine' as qs_a0, nam as qs_loc, f_code_des as qs_type, soc as qs_a0_lc FROM builtupa" pse_localities.shp ../global_map/b_core_priority/pse/builtupa.shp
	
pse_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PSE' as qs_adm0_a3, 'Palestine' as qs_adm0, 'adm1' as qs_level, 'GlobalMap' as qs_source, 'PS' as qs_iso_cc, 'Palestine' as qs_a0, laa as qs_a1, nam as qs_a1, f_code_des as qs_type, coc as qs_a0_lc FROM polbnda" pse_adm1.shp ../global_map/b_core_priority/pse/polbnda.shp
	
pse_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'PSE' as qs_adm0_a3, 'Palestine' as qs_adm0, 'adm0' as qs_level, 'GlobalMap' as qs_source, 'PS' as qs_iso_cc, 'Palestine' as qs_a0, coc as qs_a0_lc FROM polbnda" pse_adm0.shp ../global_map/b_core_priority/pse/polbnda.shp
	
	#dissolve-shapes.py -i pse_adm0.shp -o pse_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a0_lc



# SOUTH AFRICA

zaf_localities.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ZAF' as qs_adm0_a3, 'South Africa' as qs_adm0, 'locality' as qs_level, 'GlobalMap' as qs_source, nam as qs_loc, f_code_des as qs_type, soc as qs_a0_lc, 'ZA' as qs_iso_cc, 'South Africa' as qs_a0 FROM builtupa" zaf_localities.shp ../global_map/b_core_priority/zaf/zaf_1_0/builtupa.shp
	
zaf_adm2.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ZAF' as qs_adm0_a3, 'South Africa' as qs_adm0, 'adm2' as qs_level, 'GlobalMap' as qs_source, laa as qs_a2, nam as qs_a1, f_code_des as qs_type, coc as qs_a0_lc, 'ZA' as qs_iso_cc, 'South Africa' as qs_a0 FROM polbnda" zaf_adm2.shp ../global_map/b_core_priority/zaf/zaf_1_0/polbnda.shp

zaf_adm1.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ZAF' as qs_adm0_a3, 'South Africa' as qs_adm0, 'adm1' as qs_level, 'GlobalMap' as qs_source, 'ZA' as qs_iso_cc, 'South Africa' as qs_a0, nam as qs_a1, coc as qs_a0_lc FROM polbnda" zaf_adm1.shp ../global_map/b_core_priority/zaf/zaf_1_0/polbnda.shp

	#dissolve-shapes.py -i zaf_adm1.shp -o zaf_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a1,qs_a0_lc

zaf_adm0.shp:
	ogr2ogr -overwrite -f "ESRI Shapefile" -lco ENCODING="UTF-8" -sql "SELECT 'ZAF' as qs_adm0_a3, 'South Africa' as qs_adm0, 'adm0' as qs_level, 'GlobalMap' as qs_source, coc as qs_a0_lc, 'ZA' as qs_iso_cc, 'South Africa' as qs_a0 FROM polbnda" zaf_adm0.shp ../global_map/b_core_priority/zaf/zaf_1_0/polbnda.shp

	#dissolve-shapes.py -i zaf_adm1.shp -o zaf_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_a0,qs_a0_lc





#GERMANY
#No NMA open data available.

deu_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'DEU' as qs_adm0_a3, 'Germany' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, src.SHN2 as qs_a2r_lc, src.SHN3 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" deu_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/DE/PolbndA.shp

deu_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'DEU' as qs_adm0_a3, 'Germany' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM deu_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" deu_adm1.shp deu_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM deu_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" deu_adm1.shp deu_adm1.shp
	
	
deu_adm2_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT * FROM deu_adm1 src WHERE qs_a2r_lc NOT IN ('N_A') AND qs_a1_lc NOT IN ('DE140000000000')" deu_adm2_region.shp deu_adm1.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'DEU' as qs_adm0_a3, 'Germany' as qs_adm0, 'adm2_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2r, namefile.NAMA as qs_a2r_alt, namefile.ISN as qs_type FROM deu_adm2_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2r_lc = namefile.SHN" deu_adm2_region.shp deu_adm2_region.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2r as qs_a2r, src.qs_a2r_alt as qs_a2r_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM deu_adm2_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" deu_adm2_region.shp deu_adm2_region.shp


deu_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'DEU' as qs_adm0_a3, 'Germany' as qs_adm0, 'adm2_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2r, namefile.NAMA as qs_a2r_alt, namefile.ISN as qs_type FROM deu_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2r_lc = namefile.SHN WHERE src.qs_a1_lc NOT IN ('DE140000000000')" deu_adm2.shp deu_adm1.shp
	# Add in nulled qs_a2_lc from Sachsen (qs_a2r was dissolved in 2012)
	ogr2ogr -f "ESRI Shapefile" -append -sql "SELECT 'DEU' as qs_adm0_a3, 'Germany' as qs_adm0, 'adm2_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, 'N_A' as qs_a2r_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt FROM deu_adm1 src WHERE src.qs_a1_lc IN ('DE140000000000')" deu_adm2.shp deu_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2r as qs_a2r, src.qs_a2r_alt as qs_a2r_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM deu_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" deu_adm2.shp deu_adm2.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'DEU' as qs_adm0_a3, 'Germany' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2r as qs_a2r, src.qs_a2r_alt as qs_a2r_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM deu_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" deu_adm2.shp deu_adm2.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2r_lc as qs_a2r_lc, src.qs_a2r as qs_a2r, src.qs_a2r_alt as qs_a2r_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt,namefile.DESN as qs_type FROM deu_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" deu_adm2.shp deu_adm2.shp





#FINLAND
#No NMA data researched

fin_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'FIN' as qs_adm0_a3, 'Finland' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN WHERE src.SHN2 != 'FI721000'" fin_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/FI/PolbndA.shp

fin_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'FIN' as qs_adm0_a3, 'Finland' as qs_adm0, 'adm1_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM fin_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN WHERE src.qs_a1_lc != 'FI721000'" fin_adm1_region.shp fin_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.DESN as qs_type FROM fin_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" fin_adm1_region.shp fin_adm1_region.shp
	
fin_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'FIN' as qs_adm0_a3, 'Finland' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM fin_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN WHERE src.qs_a1_lc != 'FI721000'" fin_adm1.shp fin_adm1_region.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt,  namefile.DESN as qs_type FROM fin_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" fin_adm1.shp fin_adm1.shp


#ALAND
#No NMA data researched

ald_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'ALD' as qs_adm0_a3, 'Aland' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, 'Aland' as qs_a0, src.SHN2 as qs_a0_lc, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN2 = namefile.SHN WHERE src.SHN2 = 'FI721000'" ald_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/FI/PolbndA.shp


#HUNGARY
#No NMA data researched
# Different than Natural Earth for adm-1 in the separate towns are not broken out

hun_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'HUN' as qs_adm0_a3, 'Hungary' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" hun_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/HU/PolbndA.shp

hun_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'HUN' as qs_adm0_a3, 'Hungary' as qs_adm0, 'adm1_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM hun_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" hun_adm1_region.shp hun_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, namefile.DESN as qs_type FROM hun_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" hun_adm1_region.shp hun_adm1_region.shp

hun_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'HUN' as qs_adm0_a3, 'Hungary' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM hun_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" hun_adm1.shp hun_adm1_region.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM hun_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" hun_adm1.shp hun_adm1.shp







#DENMARK
#No NMA data researched

dnk_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -spat 4.7 59.7 16.8 52.8 -sql "SELECT 'DNK' as qs_adm0_a3, 'Denmark' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" dnk_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/DK/PolbndA.shp

dnk_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'DNK' as qs_adm0_a3, 'Denmark' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM dnk_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" dnk_adm1.shp dnk_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM dnk_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" dnk_adm1.shp dnk_adm1.shp


#GREENLAND
#No NMA data researched

grl_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -spat -77.508217 90.409735 -8.5 49.443491 -sql "SELECT 'GRL' as qs_adm0_a3, 'Greenland' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" grl_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/DK/PolbndA.shp

grl_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'GRL' as qs_adm0_a3, 'Greenland' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM grl_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" grl_adm1.shp grl_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM grl_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" grl_adm1.shp grl_adm1.shp


#FAROE ISLANDS
#No NMA data researched

fro_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -spat -8.5 63 -5.5 60 -sql "SELECT 'FRO' as qs_adm0_a3, 'Faroe Islands' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" fro_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/DK/PolbndA.shp



#NORWAY
#No NMA data researched

nor_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'NOR' as qs_adm0_a3, 'Norway' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" nor_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/NO/PolbndA.shp

nor_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'NOR' as qs_adm0_a3, 'Norway' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM nor_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" nor_adm1.shp nor_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM nor_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" nor_adm1.shp nor_adm1.shp


#SWEDEN
#No NMA data researched

swe_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'SWE' as qs_adm0_a3, 'Sweden' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" swe_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/SE/PolbndA.shp

swe_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'SWE' as qs_adm0_a3, 'Sweden' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM swe_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" swe_adm1.shp swe_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM swe_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" swe_adm1.shp swe_adm1.shp


#ESTONIA
#No NMA data researched

est_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'EST' as qs_adm0_a3, 'Estonia' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" est_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/EE/PolbndA.shp

est_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'EST' as qs_adm0_a3, 'Estonia' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM est_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" est_adm1.shp est_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM est_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" est_adm1.shp est_adm1.shp


#LATVIA
#No NMA data researched

lva_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'LVA' as qs_adm0_a3, 'Latvia' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" lva_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/LV/PolbndA.shp

lva_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'LVA' as qs_adm0_a3, 'Latvia' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM lva_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" lva_adm1.shp lva_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM lva_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" lva_adm1.shp lva_adm1.shp


#ROMANIA
#No NMA data researched

rou_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'ROU' as qs_adm0_a3, 'Romania' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" rou_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/RO/PolbndA.shp

rou_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'ROU' as qs_adm0_a3, 'Romania' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM rou_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" rou_adm1.shp rou_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM rou_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" rou_adm1.shp rou_adm1.shp


#IRELAND
#No NMA data researched

irl_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'IRL' as qs_adm0_a3, 'Ireland' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" irl_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/IE/PolbndA.shp

irl_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'IRL' as qs_adm0_a3, 'Ireland' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM irl_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" irl_adm1.shp irl_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM irl_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" irl_adm1.shp irl_adm1.shp


#CROATIA
#No NMA data researched

hrv_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'HRV' as qs_adm0_a3, 'Croatia' as qs_adm0, 'adm0' as qs_level, 'HR' as qs_iso_cc, 'Croatia' as qs_a0, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" hrv_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/HR/PolbndA.shp

hrv_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'HRV' as qs_adm0_a3, 'Croatia' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, 'Croatia' as qs_a0, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM hrv_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" hrv_adm1.shp hrv_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, 'Croatia' as qs_a0, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM hrv_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" hrv_adm1.shp hrv_adm1.shp


#MOLDOVA
#No NMA data researched

mda_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'MDA' as qs_adm0_a3, 'Moldova' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" mda_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/MD/PolbndA.shp

mda_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'MDA' as qs_adm0_a3, 'Moldova' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM mda_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" mda_adm1.shp mda_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM mda_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" mda_adm1.shp mda_adm1.shp


#CZECH REPUBLIC
#No NMA data researched

cze_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'CZE' as qs_adm0_a3, 'Czech Republic' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" cze_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/CZ/PolbndA.shp

cze_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'CZE' as qs_adm0_a3, 'Czech Republic' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM cze_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" cze_adm1.shp cze_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM cze_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" cze_adm1.shp cze_adm1.shp



#MALTA
#No NMA data researched

mlt_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'MLT' as qs_adm0_a3, 'Malta' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" mlt_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/MT/PolbndA.shp

mlt_adm1.shp: mlt_adm0.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'MLT' as qs_adm0_a3, 'Malta' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM mlt_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" mlt_adm1.shp mlt_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM mlt_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" mlt_adm1.shp mlt_adm1.shp





#POLAND
#No NMA data researched

pol_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'POL' as qs_adm0_a3, 'Poland' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, src.SHN2 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" pol_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/PL/PolbndA.shp

pol_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'POL' as qs_adm0_a3, 'Poland' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source,src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM pol_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" pol_adm1.shp pol_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM pol_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" pol_adm1.shp pol_adm1.shp

pol_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'POL' as qs_adm0_a3, 'Poland' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM pol_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" pol_adm2.shp pol_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt, namefile.DESN as qs_type FROM pol_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" pol_adm2.shp pol_adm2.shp

#AUSTRIA
#No NMA data researched

aut_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'AUT' as qs_adm0_a3, 'Austria' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, src.SHN2 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" aut_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/AT/PolbndA.shp

aut_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'AUT' as qs_adm0_a3, 'Austria' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM aut_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" aut_adm1.shp aut_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM aut_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" aut_adm1.shp aut_adm1.shp
	
	
aut_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'AUT' as qs_adm0_a3, 'Austria' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM aut_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" aut_adm2.shp aut_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt, namefile.DESN as qs_type FROM aut_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" aut_adm2.shp aut_adm2.shp

#SLOVAKIA
#No NMA data researched

svk_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'SVK' as qs_adm0_a3, 'Slovakia' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, src.SHN2 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" svk_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/SK/PolbndA.shp

svk_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'SVK' as qs_adm0_a3, 'Slovakia' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM svk_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" svk_adm1.shp svk_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM svk_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" svk_adm1.shp svk_adm1.shp


svk_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'SVK' as qs_adm0_a3, 'Slovakia' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM svk_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" svk_adm2.shp svk_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt, namefile.DESN as qs_type FROM svk_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" svk_adm2.shp svk_adm2.shp


#LITHUANIA
#No NMA data researched

ltu_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'LTU' as qs_adm0_a3, 'Lithuania' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, src.SHN2 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" ltu_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/LT/PolbndA.shp

ltu_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'LTU' as qs_adm0_a3, 'Lithuania' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM ltu_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" ltu_adm1.shp ltu_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM ltu_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" ltu_adm1.shp ltu_adm1.shp


ltu_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'LTU' as qs_adm0_a3, 'Lithuania' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM ltu_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" ltu_adm2.shp ltu_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt, namefile.DESN as qs_type FROM ltu_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" ltu_adm2.shp ltu_adm2.shp


#UKRAINE
#No NMA data researched

ukr_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'UKR' as qs_adm0_a3, 'Ukraine' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, src.SHN2 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" ukr_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/UA/PolbndA.shp

ukr_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'UKR' as qs_adm0_a3, 'Ukraine' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM ukr_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" ukr_adm1.shp ukr_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM ukr_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" ukr_adm1.shp ukr_adm1.shp


ukr_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'UKR' as qs_adm0_a3, 'Ukraine' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM ukr_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" ukr_adm2.shp ukr_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt, namefile.DESN as qs_type FROM ukr_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" ukr_adm2.shp ukr_adm2.shp




#GREECE
#No NMA data researched
# The 13+1 regions are shown, but the EuroGlobalMap data has a division between region and municipality that doesn't make sense. Holdover from pre-2011 reform?
# !!! Character encoding issues

grc_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'GRC' as qs_adm0_a3, 'Greece' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, 'Ελλάδα' as qs_a0, 'Elláda' as qs_a0_alt, 'XWRA' as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src" grc_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/GR/PolbndA.shp

grc_adm1.shp: grc_adm0.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'GRC' as qs_adm0_a3, 'Greece' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM grc_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" grc_adm1.shp grc_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM grc_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" grc_adm1.shp grc_adm1.shp

#BULGARIA
#No NMA data researched
# !!! Character encoding issues

bgr_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'BGR' as qs_adm0_a3, 'Bulgaria' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" bgr_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/BG/PolbndA.shp

bgr_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'BGR' as qs_adm0_a3, 'Bulgaria' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM bgr_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" bgr_adm1.shp bgr_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM bgr_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" bgr_adm1.shp bgr_adm1.shp


#CYPRUS
#No NMA data researched
# !!! Character encoding issues
# !!! Mismatch on Natural Earth adm-1

cyp_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'CYP' as qs_adm0_a3, 'Cyprus' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" cyp_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/CY/PolbndA.shp

cyp_adm1.shp: cyp_adm0_tmp.shp
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'CYP' as qs_adm0_a3, 'Cyprus' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM cyp_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" cyp_adm1.shp cyp_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM cyp_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" cyp_adm1.shp cyp_adm1.shp




#SPECIAL

#SERBIA
#Serbia - two regions
#Kosovo needs to be split off
# !! Something stupid is happening between 3 and 4. They should really be combined?

srb_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'SRB' as qs_adm0_a3, 'Serbia' as qs_adm0, 'adm0' as qs_level, 'RS' as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN WHERE src.SHN1 != 'RS2000000'" srb_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/RS/PolbndA.shp

srb_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'SRB' as qs_adm0_a3, 'Serbia' as qs_adm0, 'adm1_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM srb_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" srb_adm1_region.shp srb_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, namefile.DESN as qs_type FROM srb_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" srb_adm1_region.shp srb_adm1_region.shp

srb_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'SRB' as qs_adm0_a3, 'Serbia' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM srb_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" srb_adm1.shp srb_adm1_region.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM srb_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" srb_adm1.shp srb_adm1.shp

#KOSOVO
# Looks to be pre redo of adm-1 (still Serb view)

kos_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'KOS' as qs_adm0_a3, 'Kosovo' as qs_adm0, 'adm0' as qs_level, 'EuroGlobalMap' as qs_source, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN WHERE src.SHN1 = 'RS2000000'" kos_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/RS/PolbndA.shp


#BELGIUM
# NMA open data not investigated
#Belgium - 3 regions
#0 is a0
#1 is a1r
#2 is a1
#3 is a2

bel_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'BEL' as qs_adm0_a3, 'Belgium' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN1 as qs_a1r_lc, src.SHN2 as qs_a1_lc, src.SHN3 as qs_a2_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" bel_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/BE/PolbndA.shp

bel_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'BEL' as qs_adm0_a3, 'Belgium' as qs_adm0, 'adm1_region' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1r, namefile.NAMA as qs_a1r_alt, namefile.ISN as qs_type FROM bel_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1r_lc = namefile.SHN" bel_adm1_region.shp bel_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM bel_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" bel_adm1_region.shp bel_adm1_region.shp


bel_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'BEL' as qs_adm0_a3, 'Belgium' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM bel_adm1_region src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" bel_adm1.shp bel_adm1_region.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, namefile.DESN as qs_type FROM bel_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" bel_adm1.shp bel_adm1.shp

bel_adm2.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'BEL' as qs_adm0_a3, 'Belgium' as qs_adm0, 'adm2' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a2_lc as qs_a2_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.NAMN as qs_a2, namefile.NAMA as qs_a2_alt, namefile.ISN as qs_type FROM bel_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a2_lc = namefile.SHN" bel_adm2.shp bel_adm1.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1r_lc as qs_a1r_lc, src.qs_a1r as qs_a1r, src.qs_a1r_alt as qs_a1r_alt, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, src.qs_a2_lc as qs_a2_lc, src.qs_a2 as qs_a2, src.qs_a2_alt as qs_a2_alt, namefile.DESN as qs_type FROM bel_adm2 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" bel_adm2.shp bel_adm2.shp


#PORTUGAL
# NMA open data not investigated
# !! Portugal needs sh2 mapped as adm1; there should be regions but those aren't coded in the EuroGlobalMap

prt_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'PRT' as qs_adm0_a3, 'Portugal' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, src.SHN2 as qs_a1_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" prt_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/PT/PolbndA.shp

prt_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'PRT' as qs_adm0_a3, 'Portugal' as qs_adm0, 'adm1' as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, namefile.NAMN as qs_a1, namefile.NAMA as qs_a1_alt, namefile.ISN as qs_type FROM prt_adm0 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.qs_a1_lc = namefile.SHN" prt_adm1.shp prt_adm0.shp
	# add in the qs_type
	ogr2ogr -f "Esri Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.qs_adm0_a3 as qs_adm0_a3, src.qs_adm0 as qs_adm0, src.qs_level as qs_level, src.qs_source as qs_source, src.qs_iso_cc as qs_iso_cc, src.qs_a0 as qs_a0, src.qs_a0_alt as qs_a0_alt, src.qs_a0_lc as qs_a0_lc, src.qs_a1_lc as qs_a1_lc, src.qs_a1 as qs_a1, src.qs_a1_alt as qs_a1_alt, namefile.DESN as qs_type FROM prt_adm1 src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_ISN.dbf'.EBM_ISN namefile ON src.qs_type = namefile.ISN" prt_adm1.shp prt_adm1.shp



#GEORGIA

geo_adm0.shp:
	# GE Georgia geo
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'GEO' as qs_adm0_a3, 'Georgia' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" geo_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/GE/PolbndA.shp
	
	
# LUXEMBOURG
	
lux_adm0.shp:
	# LU Luxembourg lux
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'LUX' as qs_adm0_a3, 'Luxembourg' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" lux_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/LU/PolbndA.shp


# ICELAND
# EuroGlobalMap is out of date per adm-1

isl_adm0.shp:
	# IS Iceland isl
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'ISL' as qs_adm0_a3, 'Iceland' as qs_adm0, 'adm0' as qs_level, src.ICC as qs_iso_cc, src.SHN0 as qs_a0_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" isl_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/IS/PolbndA.shp


# SLOVENIA

svn_adm0.shp: 
	# SI Slovenia svn
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -s_srs EPSG:4019 -t_srs EPSG:4326 -sql "SELECT 'SVN' as qs_adm0_a3, 'Slovenia' as qs_adm0, 'adm0' as qs_level, 'SI' as qs_iso_cc, src.SHN0 as qs_a0_lc, namefile.NAMN as qs_a0, namefile.NAMA as qs_a0_alt, namefile.ISN as qs_type, 'EuroGlobalMap' as qs_source FROM PolbndA src LEFT JOIN '../nma/global_map/EGM_5-1SHP_20120704/DATA/Full_Europe/EBM_NAM.dbf'.EBM_NAM namefile ON src.SHN0 = namefile.SHN" svn_adm0.shp ../nma/global_map/EGM_5-1SHP_20120704/DATA/Countries/SI/PolbndA.shp


ne_adm1.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.adm0_a3 as qs_adm0_a3, src.admin as qs_adm0, 'adm1' as qs_level, src.iso_a2 as qs_iso_cc, src.iso_a2 as qs_a0_lc, src.admin as qs_a0, src.name as qs_a1, src.adm1_code as qs_a1_lc, src.region as qs_a1r, src.region_cod as qs_a1r_lc, src.type_en as qs_type, 'Natural Earth' as qs_source, woe_id as qs_woe_id, gn_id as qs_gn_id, 4000000 as qs_scale FROM ne_10m_admin_1_states_provinces src WHERE (src.adm0_a3 not in ('AUS','AUT','BEL','BGR','BRA','CAN','CHL','CHE','CYP','CZE','DEU','DNK','ESP','EST','FIN','FRA','GBR','GIB','GRC','GRL','HRV','HUN','IRL','ITA','LIE','LTU','LVA','MCO','MDA','MEX','MLT','NLD','NOR','NZL','POL','PRI','PRT','PSE','ROU','RUS','SRB','SVK','SWE','USA','UKR','VAT','ZAF') or src.gu_a3 in ('NSV', 'MTQ', 'GUF', 'REU', 'MYT', 'GLP') or src.adm1_code IN ('NLD-5148', 'NLD-5149','FRA-1442','FRA-2000','FRA-4601','FRA-4602','FRA-4603','SPM-4866')) and src.featurecla IN ('Admin-1 scale rank')" ne_adm1.shp ../natural_earth/ne_10m_admin_1_states_provinces.shp
	ogr2ogr -f "ESRI Shapefile" -append -sql "SELECT src.adm0_a3 as qs_adm0_a3, src.admin as qs_adm0, 'adm1' as qs_level, src.iso_a2 as qs_iso_cc, src.iso_a2 as qs_a0_lc, src.admin as qs_a0, src.name as qs_a1, src.adm1_code as qs_a1_lc, src.region as qs_a1r, src.region_cod as qs_a1r_lc, featurecla as qs_type, 'Natural Earth' as qs_source, woe_id as qs_woe_id, gn_id as qs_gn_id, 4000000 as qs_scale FROM ne_10m_admin_1_states_provinces src WHERE (src.adm0_a3 not in ('AUS','AUT','BEL','BGR','BRA','CAN','CHL','CHE','CYP','CZE','DEU','DNK','ESP','EST','FIN','FRA','GBR','GIB','GRC','GRL','HRV','HUN','IRL','ITA','LIE','LTU','LVA','MCO','MDA','MEX','MLT','NLD','NOR','NZL','POL','PRI','PRT','PSE','ROU','RUS','SRB','SVK','SWE','USA','UKR','VAT','ZAF') or src.gu_a3 in ('NSV', 'MTQ', 'GUF', 'REU', 'MYT', 'GLP') or src.adm1_code IN ('NLD-5148', 'NLD-5149','FRA-1442','FRA-2000','FRA-4601','FRA-4602','FRA-4603','SPM-4866')) and src.featurecla NOT IN ('Admin-1 scale rank')" ne_adm1.shp ../natural_earth/ne_10m_admin_1_states_provinces.shp
# Needs work, and a dissolve

ne_adm1_region.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.adm0_a3 as qs_adm0_a3, src.name as qs_adm0, 'adm1_region' as qs_level, src.iso_a2 as qs_iso_cc, src.iso_a2 as qs_a0_lc, src.admin as qs_a0, src.name as qs_a1, src.adm1_code as qs_a1_lc, src.region as qs_a1r, src.region_cod as qs_a1r_lc, src.type_en as qs_type, 'Natural Earth' as qs_source, woe_id as qs_woe_id, gn_id as qs_gn_id, 4000000 as qs_scale FROM ne_10m_admin_1_states_provinces src WHERE src.adm0_a3 not in ('BEL','ESP','FIN','FRA','GBR','HUN','ITA','SRB') or src.region IS NOT NULL" ne_adm1_region.shp ../natural_earth/ne_10m_admin_1_states_provinces.shp

ussd_adm0.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT src.adm0_a3 as qs_adm0_a3, src.admin as qs_adm0, 'adm0' as qs_level, src.iso_a2 as qs_iso_cc, src.admin as qs_a0, src.br_name as qs_a0_alt, 'US State Department, with Natural Earth mods' as qs_source, woe_adm0 as qs_woe_id, 200000 as qs_scale FROM us_state_department_countries_ne_hybrid src WHERE src.adm0_a3 not in ('aus','ald','aut','bel','bgr','bra','can','che','chl','cze','deu','dnk','esp','est','fin','fra','fro','gbr','geo','gib','grc','grl','hrv','hun','irl','isl','ita','kos','lie','ltu','lux','lva','mco','mda','mex','mlt','nld','nor','nzl','pol','pri','prt','pse','rou','srb','smr','svk','svn','swe','usa','ukr','zaf') or src.gu_a3 IN ('NLY','GUF','GLP','MTQ','REU','MYT')" ussd_adm0.shp ../us_state_department/final_data/us_state_department_countries_ne_hybrid.shp



raw_downloads: \
	raw_downloads/tl_2010_us_place10.shp \	
	raw_downloads/tl_2010_us_county10.shp \
	raw_downloads/tl_2010_us_state10.shp \


raw_downloads/Place_2010Census_DP1.shp:
	wget http://www2.census.gov/geo/tiger/TIGER2010DP1/Place_2010Census_DP1.zip -O raw_downloads/Place_2010Census_DP1.zip
	unzip -o raw_downloads/Place_2010Census_DP1.zip -d raw_downloads/
	rm raw_downloads/Place_2010Census_DP1.zip

raw_downloads/tl_2010_us_county10.shp:
	wget ftp://ftp2.census.gov/geo/tiger/TIGER2010/COUNTY/2010/tl_2010_us_county10.zip -O raw_downloads/tl_2010_us_county10.zip
	unzip -o raw_downloads/tl_2010_us_county10.zip -d raw_downloads/
	rm raw_downloads/tl_2010_us_county10.zip
	wget http://www2.census.gov/geo/tiger/TIGER2010DP1/County_2010Census_DP1.zip -O raw_downloads/County_2010Census_DP1.zip
	unzip -o raw_downloads/County_2010Census_DP1.zip -d raw_downloads/
	rm raw_downloads/County_2010Census_DP1.zip

raw_downloads/tl_2010_us_state10.shp:
	wget ftp://ftp2.census.gov/geo/tiger/TIGER2010/STATE/2010/tl_2010_us_state10.zip -O raw_downloads/tl_2010_us_state10.zip
	unzip -o raw_downloads/tl_2010_us_state10.zip -d raw_downloads/
	rm raw_downloads/tl_2010_us_state10.zip
	wget http://www2.census.gov/geo/tiger/TIGER2010DP1/State_2010Census_DP1.zip -O raw_downloads/State_2010Census_DP1.zip
	unzip -o raw_downloads/State_2010Census_DP1.zip -d raw_downloads/
	rm raw_downloads/State_2010Census_DP1.zip

raw_downloads/CouSub_2010Census_DP1.shp:
	wget http://www2.census.gov/geo/tiger/TIGER2010DP1/CouSub_2010Census_DP1.zip -O raw_downloads/CouSub_2010Census_DP1.zip
	unzip -o raw_downloads/CouSub_2010Census_DP1.zip -d raw_downloads/
	rm raw_downloads/CouSub_2010Census_DP1.zip
	
raw_downloads/usa_localadmin_all.shp:
	# Connecticut
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_09_060_00_500k.zip -O raw_downloads/gz_2010_06_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_06_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_06_060_00_500k.zip
	# Illinois
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_17_060_00_500k.zip -O raw_downloads/gz_2010_17_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_17_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_17_060_00_500k.zip
	# Indiana
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_18_060_00_500k.zip -O raw_downloads/gz_2010_18_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_18_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_18_060_00_500k.zip
	# Kansas
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_20_060_00_500k.zip -O raw_downloads/gz_2010_20_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_20_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_20_060_00_500k.zip
	# Maine
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_23_060_00_500k.zip -O raw_downloads/gz_2010_23_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_23_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_23_060_00_500k.zip
	# Mass
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_25_060_00_500k.zip -O raw_downloads/gz_2010_25_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_25_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_25_060_00_500k.zip
	# Michigan
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_26_060_00_500k.zip -O raw_downloads/gz_2010_26_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_26_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_26_060_00_500k.zip
	# Minnesota
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_27_060_00_500k.zip -O raw_downloads/gz_2010_27_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_27_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_27_060_00_500k.zip
	# Missouri
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_29_060_00_500k.zip -O raw_downloads/gz_2010_29_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_29_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_29_060_00_500k.zip
	# Nebraska
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_31_060_00_500k.zip -O raw_downloads/gz_2010_31_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_31_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_31_060_00_500k.zip
	# New Hampshire
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_33_060_00_500k.zip -O raw_downloads/gz_2010_33_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_33_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_33_060_00_500k.zip
	# New Jersey
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_34_060_00_500k.zip -O raw_downloads/gz_2010_34_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_34_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_34_060_00_500k.zip
	# New York
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_36_060_00_500k.zip -O raw_downloads/gz_2010_36_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_36_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_36_060_00_500k.zip
	# North Dakota
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_38_060_00_500k.zip -O raw_downloads/gz_2010_38_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_38_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_38_060_00_500k.zip
	# Ohio
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_39_060_00_500k.zip -O raw_downloads/gz_2010_39_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_39_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_39_060_00_500k.zip
	# Penn
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_42_060_00_500k.zip -O raw_downloads/gz_2010_42_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_42_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_42_060_00_500k.zip
	# Rhode Island
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_44_060_00_500k.zip -O raw_downloads/gz_2010_44_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_44_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_44_060_00_500k.zip
	# South Dakota
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_46_060_00_500k.zip -O raw_downloads/gz_2010_46_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_46_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_46_060_00_500k.zip
	# Vermont
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_50_060_00_500k.zip -O raw_downloads/gz_2010_50_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_50_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_50_060_00_500k.zip
	# Wisconsin
	wget http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_55_060_00_500k.zip -O raw_downloads/gz_2010_55_060_00_500k.zip
	unzip -o raw_downloads/gz_2010_55_060_00_500k.zip -d raw_downloads/
	rm raw_downloads/gz_2010_55_060_00_500k.zip
	#
	# Merge the 9 states with no overlap
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_23_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_25_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_33_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_34_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_38_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_42_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_44_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_46_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_no_overlap.shp raw_downloads/gz_2010_55_060_00_500k.shp
	# Merge the 11 states with overlap
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_09_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_17_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_18_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_20_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_26_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_27_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_29_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_31_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_36_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_39_060_00_500k.shp
	ogr2ogr -f "Esri Shapefile" -append raw_downloads/usa_localadmin_with_overlap.shp raw_downloads/gz_2010_50_060_00_500k.shp
	# All together now
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" raw_downloads/usa_localadmin_all.shp raw_downloads/usa_localadmin_no_overlap.shp
	ogr2ogr -f "ESRI Shapefile" -append raw_downloads/usa_localadmin_all.shp raw_downloads/usa_localadmin_with_overlap.shp

# LOCALITIES

all_localities_quattroshapes: \
	bra_localities_qs.shp \
	idn_localities_qs.shp \
	mys_localities_qs.shp \
	tha_localities_qs.shp \
	kor_localities_qs.shp \
	twn_localities_qs.shp \
	chn_localities_qs.shp \
	ind_localities_qs.shp \
	jpn_localities_qs.shp \
	sgp_localities_qs.shp \
	tur_localities_qs.shp \
	gbr_localities_qs.shp \
	chl_localities_qs.shp \
	rus_localities_qs.shp \
	mex_localities_qs.shp

bra_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'BRA' as qs_adm0_a3, 'BR' as qs_iso_cc, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'BR'" bra_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

idn_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'IDN' as qs_adm0_a3, 'ID' as qs_iso_cc, 'Indonesia' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'ID'" idn_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

mys_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'MYS' as qs_adm0_a3, 'MY' as qs_iso_cc, 'Malaysia' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'MY'" mys_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

tha_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'THA' as qs_adm0_a3, 'TH' as qs_iso_cc, 'Thailand' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'TH'" tha_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

kor_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'KOR' as qs_adm0_a3, 'KR' as qs_iso_cc, 'South Korea' as qs_adm0, '한국' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'KR'" kor_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

twn_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'TWN' as qs_adm0_a3, 'TW' as qs_iso_cc, 'Taiwan' as qs_adm0, '臺灣' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'TW'" twn_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

chn_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'CHN' as qs_adm0_a3, 'CN' as qs_iso_cc, 'China' as qs_adm0, '中國' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'CN'" chn_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

ind_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'IND' as qs_adm0_a3, 'IN' as qs_iso_cc, 'India' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'IN'" ind_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

aus_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'AUS' as qs_adm0_a3, 'AU' as qs_iso_cc, 'Australia' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'AU'" aus_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

jpn_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'JPN' as qs_adm0_a3, 'JP' as qs_iso_cc, 'Japan' as qs_adm0, '日本' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'JP'" jpn_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

sgp_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'SGP' as qs_adm0_a3, 'SG' as qs_iso_cc, 'Singapore' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'SG'" sgp_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

gbr_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'GBR' as qs_adm0_a3, 'GB' as qs_iso_cc, 'United Kingdom' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'GB'" gbr_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

tur_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'TUR' as qs_adm0_a3, 'TR' as qs_iso_cc, 'Turkey' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'TR'" tur_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

chl_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'CHL' as qs_adm0_a3, 'CL' as qs_iso_cc, 'Chile' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'CL'" chl_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

rus_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'RUS' as qs_adm0_a3, 'RU' as qs_iso_cc, 'Russia' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'RU'" rus_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp

mex_localities_qs.shp:
	ogr2ogr -f "ESRI Shapefile" -overwrite -lco ENCODING="UTF-8" -sql "SELECT 'MEX' as qs_adm0_a3, 'MX' as qs_iso_cc, 'Mexico' as qs_a0, name as qs_loc_alt, gn_id as qs_loc_lc, 'locality' as qs_level, 'quattroshapes' as qs_source, gn_id, gn_name as qs_loc, gn_fcode, gn_adm0_cc, gn_namadm1, gn_pop, woe_id, woe_adm0, woe_adm1, woe_adm2, woe_lau, woe_local, name_en as qs_loc_alt2, name_adm0 as qs_a0, name_adm1 as qs_a1, name_adm2 as qs_a2, name_lau as qs_la, woe_vers, placetype as qs_type, quad_count, photo_sum, photo_max FROM quattroshapes_localities_priority_and_extras_master_post_diss_attr2 WHERE gn_adm0_cc = 'MX'" mex_localities_qs.shp quattroshapes/quattroshapes_localities_priority_and_extras_master_post_diss_attr2.shp



clean:
	mkdir -p raw_downloads
	rm -f all_localities.*
	rm -f all_localadmin.*
	rm -f all_adm0.*
	rm -f all_adm1_region.*
	rm -f all_adm1.*
	rm -f all_adm2_region.*
	rm -f all_adm2.*
	
deep-clean:
	rm -f *.shp *.shx *.dbf *.prj *.cpg