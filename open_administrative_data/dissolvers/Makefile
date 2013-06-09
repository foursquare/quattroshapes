all: dissolve
	touch all

dissolve: \
	dissolve-adm0 \
	dissolve-adm1-region \
	dissolve-adm1 \
	dissolve-adm2-region \
	dissolve-adm2 \
	dissovle-localadmin \
	dissolve-localities
	
	touch dissolve
		
dissolve-adm0: \
	../aut_adm0.shp \
	../bra_adm0.shp \
	../bel_adm0.shp \
	../cyp_adm0.shp \
	../deu_adm0.shp \
	../fin_adm0.shp \
	../fra_adm0.shp \
	../fro_adm0.shp \
	../hun_adm0.shp \
	../ltu_adm0.shp \
	../pol_adm0.shp \
	../srb_adm0.shp \
	../svk_adm0.shp \
	../ukr_adm0.shp \
	../ltu_adm0.shp \
	../bgr_adm0.shp \
	../cze_adm0.shp \
	../dnk_adm0.shp \
	../esp_adm0.shp \
	../est_adm0.shp \
	../fin_adm0.shp \
	../gbr_adm0.shp \
	../grc_adm0.shp \
	../grl_adm0.shp \
	../hrv_adm0.shp \
	../irl_adm0.shp \
	../isl_adm0.shp \
	../ita_adm0.shp \
	../kos_adm0.shp \
	../lva_adm0.shp \
	../mlt_adm0.shp \
	../mda_adm0.shp \
	../nld_adm0.shp \
	../nor_adm0.shp \
	../prt_adm0.shp \
	../rou_adm0.shp \
	../swe_adm0.shp \
	../usa_adm0.shp \
	../aus_adm0.shp \
	../nzl_adm0.shp \
	../che_adm0.shp \
	../lie_adm0.shp \
	../chl_adm0.shp \
	../pse_adm0.shp \
	../mex_adm0.shp \
	../zaf_adm0.shp \
	../ussd_adm0.shp
	
	touch dissolve-adm0
	
	#../idn_adm0.shp \
	#../rus_adm0.shp \
	
dissolve-adm1-region: \
	../gbr_adm1_region.shp \
	../bel_adm1_region.shp \
	../fin_adm1_region.shp \
	../fra_adm1_region.shp \
	../hun_adm1_region.shp \
	../srb_adm1_region.shp
	
	touch dissolve-adm1-region
	
dissolve-adm1: \
	../aut_adm1.shp \
	../bel_adm1.shp \
	../bra_adm1.shp \
	../can_adm1.shp \
	../dnk_adm1.shp \
	../grl_adm1.shp \
	../gbr_adm1.shp \
	../deu_adm1.shp \
	../nzl_adm1.shp \
	../hrv_adm1.shp \
	../gbr_adm1.shp \
	../fra_adm1.shp \
	../grc_adm1.shp \
	../rus_adm1.shp \
	../srb_adm1.shp \
	../svk_adm1.shp \
	../pol_adm1.shp \
	../ukr_adm1.shp \
	../ltu_adm1.shp \
	../aus_adm1.shp \
	../che_adm1.shp \
	../lie_adm1.shp \
	../chl_adm1.shp \
	../zaf_adm1.shp

	touch dissolve-adm1
	
dissolve-adm2-region: \
	../deu_adm2_region.shp
	
	touch dissolve-adm2-region

dissolve-adm2: \
	../aus_adm2.shp \
	../che_adm2.shp \
	../chl_adm2.shp \
	../idn_adm2.shp \
	../zaf_adm2.shp
	
	touch dissolve-adm2

dissovle-localadmin: \
	../gbr_localadmin.shp
	
	touch dissovle-localadmin

dissolve-localities: \
	../bra_localities_qs.shp \
	../idn_localities.shp \
	../mys_localities.shp \
	../tha_localities.shp \
	../kor_localities.shp \
	../twn_localities.shp \
	../chn_localities.shp \
	../ind_localities.shp \
	../aus_localities.shp \
	../jpn_localities.shp \
	../sgp_localities.shp \
	../chl_localities_qs.shp \
	../rus_localities_qs.shp

	#../mex_localities_qs.shp	
	#../gbr_localities_qs.shp \
	#../tur_localities_qs.shp \
 	touch dissolve-localities


../gbr_localadmin.shp:
	shputils/dissolve-shapes.py -i ../gbr_localadmin.shp -o ../gbr_localadmin.shp -f qs_adm0_a3,qs_iso_cc,qs_adm0,qs_a0,qs_level,qs_source,qs_la,qs_la_lc,qs_la_lc2,qs_a1,qs_type,qs_a1r,qs_a1r_lc



../bra_localities_qs.shp:
	shputils/dissolve-shapes.py -i ../bra_localities_qs.shp -o ../bra_localities_qs.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../idn_localities.shp:
	shputils/dissolve-shapes.py -i ../idn_localities.shp -o ../idn_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../mys_localities.shp:
	shputils/dissolve-shapes.py -i ../mys_localities.shp -o ../mys_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../tha_localities.shp:
	shputils/dissolve-shapes.py -i ../tha_localities.shp -o ../tha_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../kor_localities.shp:
	shputils/dissolve-shapes.py -i ../kor_localities.shp -o ../kor_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../twn_localities.shp:
	shputils/dissolve-shapes.py -i ../twn_localities.shp -o ../twn_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../chn_localities.shp:
	shputils/dissolve-shapes.py -i ../chn_localities.shp -o ../chn_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../ind_localities.shp:
	shputils/dissolve-shapes.py -i ../ind_localities.shp -o ../ind_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../aus_localities.shp:
	shputils/dissolve-shapes.py -i ../aus_localities.shp -o ../aus_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../jpn_localities.shp:
	shputils/dissolve-shapes.py -i ../jpn_localities.shp -o ../jpn_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../sgp_localities.shp:
	shputils/dissolve-shapes.py -i ../sgp_localities.shp -o ../sgp_localities.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../gbr_localities_qs.shp:
	shputils/dissolve-shapes.py -i ../gbr_localities_qs.shp -o ../gbr_localities_qs.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../tur_localities_qs.shp:
	shputils/dissolve-shapes.py -i ../tur_localities_qs.shp -o ../tur_localities_qs.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../chl_localities_qs.shp:
	shputils/dissolve-shapes.py -i ../chl_localities_qs.shp -o ../chl_localities_qs.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../rus_localities_qs.shp:
	shputils/dissolve-shapes.py -i ../rus_localities_qs.shp -o ../rus_localities_qs.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source

../mex_localities_qs.shp:
	shputils/dissolve-shapes.py -i ../mex_localities_qs.shp -o ../mex_localities_qs.shp -f qs_adm0_a3,qs_iso_cc,qs_a0,qs_loc,qs_loc_lc,qs_level,qs_source





../usa_adm0.shp:
	shputils/dissolve-shapes.py -i ../usa_adm0.shp -o ../usa_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0

../bra_adm0.shp:
	#shputils/dissolve-shapes.py -i ../bra_adm0.shp -o ../bra_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0
	shputils/dissolve-shapes.py -i ../bra_adm0.shp -o ../bra_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_iso_cc,qs_a0,qs_source

../bra_adm1.shp:
	shputils/dissolve-shapes.py -i ../bra_adm1.shp -o ../bra_adm1.shp -f qs_adm0_a3,qs_iso_cc,qs_adm0,qs_a0,qs_a1,qs_a1_lc,qs_level,qs_source,qs_type

../aus_adm0.shp:
	shputils/dissolve-shapes.py -i ../aus_adm0.shp -o ../aus_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0

../aus_adm1.shp:
	shputils/dissolve-shapes.py -i ../aus_adm1.shp -o ../aus_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_a1_lc

../aus_adm2.shp:
	shputils/dissolve-shapes.py -i ../aus_adm2.shp -o ../aus_adm2.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_a1_lc,qs_a2,qs_a2_lc

../fro_adm0.shp:
	shputils/dissolve-shapes.py -i ../fro_adm0.shp -o ../fro_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_iso_cc,qs_a0_lc,qs_a1_lc,qs_a0,qs_a0_alt,qs_type,qs_source

../rus_adm0.shp:
	shputils/dissolve-shapes.py -i ../rus_adm0.shp -o ../rus_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0

../mex_adm0.shp:
	shputils/dissolve-shapes.py -i ../mex_adm0.shp -o ../mex_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0

../nzl_adm0.shp:
	shputils/dissolve-shapes.py -i ../nzl_adm0.shp -o ../nzl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0

../nzl_adm1.shp:
	shputils/dissolve-shapes.py -i ../nzl_adm1.shp -o ../nzl_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_a1_lc

../che_adm0.shp:
	shputils/dissolve-shapes.py -i ../che_adm0.shp -o ../che_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0

../che_adm1.shp:
	shputils/dissolve-shapes.py -i ../che_adm1.shp -o ../che_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_a1_lc,qs_type

../che_adm2.shp:
	shputils/dissolve-shapes.py -i ../che_adm2.shp -o ../che_adm2.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_a1_lc,qs_a2,qs_a2_lc,qs_type

../lie_adm0.shp:
	shputils/dissolve-shapes.py -i ../lie_adm0.shp -o ../lie_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0

../lie_adm1.shp:
	shputils/dissolve-shapes.py -i ../lie_adm1.shp -o ../lie_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1_lc

../idn_adm0.shp:
	shputils/dissolve-shapes.py -i ../idn_adm0.shp -o ../idn_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0
	#shputils/dissolve-shapes.py -i ../idn_adm0.shp -o ../idn_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc

../idn_adm1.shp:
	shputils/dissolve-shapes.py -i ../idn_adm1.shp -o ../idn_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc,qs_a1

../idn_adm2.shp:
	shputils/dissolve-shapes.py -i ../idn_adm2.shp -o ../idn_adm2.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc,qs_a1,qs_a2,qs_type

../chl_adm0.shp:
	shputils/dissolve-shapes.py -i ../chl_adm0.shp -o ../chl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc

../chl_adm1.shp:
	shputils/dissolve-shapes.py -i ../chl_adm1.shp -o ../chl_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc,qs_a0,qs_a1

../pse_adm0.shp:
	shputils/dissolve-shapes.py -i ../pse_adm0.shp -o ../pse_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc

../zaf_adm0.shp:
	shputils/dissolve-shapes.py -i ../zaf_adm0.shp -o ../zaf_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc

../zaf_adm1.shp:
	shputils/dissolve-shapes.py -i ../zaf_adm1.shp -o ../zaf_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc,qs_a1


../bel_adm1_region.shp:
	shputils/dissolve-shapes.py -i ../bel_adm1_region.shp -o ../bel_adm1_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_type

../fin_adm1_region.shp:
	shputils/dissolve-shapes.py -i ../fin_adm1_region.shp -o ../fin_adm1_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_type

../fra_adm1_region.shp:
	shputils/dissolve-shapes.py -i ../fra_adm1_region.shp -o ../fra_adm1_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_type

../gbr_adm1_region.shp:
	shputils/dissolve-shapes.py -i ../gbr_adm1_region.shp -o ../gbr_adm1_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_type

../hun_adm1_region.shp:
	shputils/dissolve-shapes.py -i ../hun_adm1_region.shp -o ../hun_adm1_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_type

../srb_adm1_region.shp:
	shputils/dissolve-shapes.py -i ../srb_adm1_region.shp -o ../srb_adm1_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_type


../aut_adm1.shp:
	shputils/dissolve-shapes.py -i ../aut_adm1.shp -o ../aut_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../bel_adm1.shp:
	#include the regions
	shputils/dissolve-shapes.py -i ../bel_adm1.shp -o ../bel_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../can_adm1.shp:
	shputils/dissolve-shapes.py -i ../can_adm1.shp -o ../can_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_type

../dnk_adm1.shp:
	shputils/dissolve-shapes.py -i ../dnk_adm1.shp -o ../dnk_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../grl_adm1.shp:
	shputils/dissolve-shapes.py -i ../grl_adm1.shp -o ../grl_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../deu_adm1.shp:
	shputils/dissolve-shapes.py -i ../deu_adm1.shp -o ../deu_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../gbr_adm1.shp:
	shputils/dissolve-shapes.py -i ../gbr_adm1.shp -o ../gbr_adm1.shp -f qs_adm0,qs_a0,qs_adm0_a3,qs_source,qs_a1r_alt,qs_level,qs_a0_alt,qs_iso_cc,qs_a0_lc,qs_a1r_lc,qs_a1,qs_type,qs_a1r,qs_a1_alt,qs_a1_lc

../fra_adm1.shp:
	shputils/dissolve-shapes.py -i ../fra_adm1.shp -o ../fra_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r_lc,qs_a1r,qs_a1r_alt,qs_a1_lc,qs_a1,qs_a1_alt,qs_type

../grc_adm1.shp:
	shputils/dissolve-shapes.py -i ../grc_adm1.shp -o ../grc_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1_lc,qs_a1,qs_a1_alt,qs_type

../srb_adm1.shp:
	#include the regions
	shputils/dissolve-shapes.py -i ../srb_adm1.shp -o ../srb_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1r,qs_a1r_alt,qs_a1r_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../svk_adm1.shp:
	shputils/dissolve-shapes.py -i ../svk_adm1.shp -o ../svk_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../pol_adm1.shp:
	shputils/dissolve-shapes.py -i ../pol_adm1.shp -o ../pol_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../rus_adm1.shp:
	shputils/dissolve-shapes.py -i ../rus_adm1.shp -o ../rus_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a1,qs_a1_alt

../ukr_adm1.shp:
	shputils/dissolve-shapes.py -i ../ukr_adm1.shp -o ../ukr_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../ltu_adm1.shp:
	shputils/dissolve-shapes.py -i ../ltu_adm1.shp -o ../ltu_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1,qs_a1_alt,qs_a1_lc,qs_type

../hrv_adm1.shp:
	shputils/dissolve-shapes.py -i ../hrv_adm1.shp -o ../hrv_adm1.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1_lc,qs_a1,qs_a1_alt,qs_type


	
../aut_adm0.shp:
	shputils/dissolve-shapes.py -i ../aut_adm0.shp -o ../aut_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type
	
../bel_adm0.shp:
	shputils/dissolve-shapes.py -i ../bel_adm0.shp -o ../bel_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../cyp_adm0.shp:
	shputils/dissolve-shapes.py -i ../cyp_adm0.shp -o ../cyp_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../deu_adm0.shp:
	shputils/dissolve-shapes.py -i ../deu_adm0.shp -o ../deu_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../fin_adm0.shp:
	shputils/dissolve-shapes.py -i ../fin_adm0.shp -o ../fin_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../fra_adm0.shp:
	shputils/dissolve-shapes.py -i ../fra_adm0.shp -o ../fra_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../hun_adm0.shp:
	shputils/dissolve-shapes.py -i ../hun_adm0.shp -o ../hun_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../ltu_adm0.shp:
	shputils/dissolve-shapes.py -i ../ltu_adm0.shp -o ../ltu_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../pol_adm0.shp:
	shputils/dissolve-shapes.py -i ../pol_adm0.shp -o ../pol_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../srb_adm0.shp:
	shputils/dissolve-shapes.py -i ../srb_adm0.shp -o ../srb_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../svk_adm0.shp:
	shputils/dissolve-shapes.py -i ../svk_adm0.shp -o ../svk_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../ukr_adm0.shp:
	shputils/dissolve-shapes.py -i ../ukr_adm0.shp -o ../ukr_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type


../bgr_adm0.shp:
	shputils/dissolve-shapes.py -i ../bgr_adm0.shp -o ../bgr_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../cze_adm0.shp:
	shputils/dissolve-shapes.py -i ../cze_adm0.shp -o ../cze_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../dnk_adm0.shp:
	shputils/dissolve-shapes.py -i ../dnk_adm0.shp -o ../dnk_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../esp_adm0.shp:
	shputils/dissolve-shapes.py -i ../esp_adm0.shp -o ../esp_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../est_adm0.shp:
	shputils/dissolve-shapes.py -i ../est_adm0.shp -o ../est_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../gbr_adm0.shp:
	shputils/dissolve-shapes.py -i ../gbr_adm0.shp -o ../gbr_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_type -c qs_a0_lc:last

../grc_adm0.shp:
	shputils/dissolve-shapes.py -i ../grc_adm0.shp -o ../grc_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../grl_adm0.shp:
	shputils/dissolve-shapes.py -i ../grl_adm0.shp -o ../grl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../hrv_adm0.shp:
	shputils/dissolve-shapes.py -i ../hrv_adm0.shp -o ../hrv_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../irl_adm0.shp:
	shputils/dissolve-shapes.py -i ../irl_adm0.shp -o ../irl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../isl_adm0.shp:
	shputils/dissolve-shapes.py -i ../isl_adm0.shp -o ../isl_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../ita_adm0.shp:
	shputils/dissolve-shapes.py -i ../ita_adm0.shp -o ../ita_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../kos_adm0.shp:
	shputils/dissolve-shapes.py -i ../kos_adm0.shp -o ../kos_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../lva_adm0.shp:
	shputils/dissolve-shapes.py -i ../lva_adm0.shp -o ../lva_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../mda_adm0.shp:
	shputils/dissolve-shapes.py -i ../mda_adm0.shp -o ../mda_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../mlt_adm0.shp:
	shputils/dissolve-shapes.py -i ../mlt_adm0.shp -o ../mlt_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../nld_adm0.shp:
	shputils/dissolve-shapes.py -i ../nld_adm0.shp -o ../nld_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../nor_adm0.shp:
	shputils/dissolve-shapes.py -i ../nor_adm0.shp -o ../nor_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../prt_adm0.shp:
	shputils/dissolve-shapes.py -i ../prt_adm0.shp -o ../prt_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type

../rou_adm0.shp:
	shputils/dissolve-shapes.py -i ../rou_adm0.shp -o ../rou_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type
	
../swe_adm0.shp:
	shputils/dissolve-shapes.py -i ../swe_adm0.shp -o ../swe_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_type
	


../deu_adm2_region.shp:
	shputils/dissolve-shapes.py -i ../deu_adm2_region.shp -o ../deu_adm2_region.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a0_alt,qs_a0_lc,qs_a1_lc,qs_a1,qs_a1_alt,qs_a2r,qs_a2r_lc,qs_a2r_alt,qs_type
	


../zaf_adm2.shp:
	shputils/dissolve-shapes.py -i ../zaf_adm2.shp -o ../zaf_adm2.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_a2,qs_a1,qs_type,qs_a0_lc,qs_iso_cc,qs_a0
	
../chl_adm2.shp:
	shputils/dissolve-shapes.py -i ../chl_adm2.shp -o ../chl_adm2.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_source,qs_iso_cc,qs_a0,qs_a2,qs_a1,qs_type



../ussd_adm0.shp:
	shputils/dissolve-shapes.py -i ../ussd_adm0.shp -o ../ussd_adm0.shp -f qs_adm0_a3,qs_adm0,qs_level,qs_iso_cc,qs_a0,qs_a0_alt,qs_source,qs_woe_id,qs_scale
