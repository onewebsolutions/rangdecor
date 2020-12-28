from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from rang_main import views



def catalogue_pvc(request) :

    current_url = resolve(request.path_info).url_name
    return redirect('catalogue', 'pvc-laminate')



def catalogue_charco(request) :

    current_url = resolve(request.path_info).url_name
    return redirect('catalogue', 'charco-charm')



def sheet_ab_84(request) :

    response = redirect('/static/images/AB-84.jpg/')
    
    return response



def sheet_ab_82(request) :

    response = redirect('/static/images/AB-82.jpg/')
    
    return response



def sheet_ab_83(request) :

    response = redirect('/static/images/AB-83.jpg/')
    
    return response



def sheet_ab_86(request) :

    response = redirect('/static/images/AB-86.jpg/')
    
    return response



def sheet_ab_85(request) :

    response = redirect('/static/images/AB-85.jpg/')
    
    return response



def sheet_ab_81(request) :

    response = redirect('/static/images/AB-81.jpg/')
    
    return response



def sheet_qp_91(request) :

    response = redirect('/static/images/QP-91.jpg/')
    
    return response



def sheet_qp_96(request) :

    response = redirect('/static/images/QP-96.jpg/')
    
    return response



def sheet_qp_92(request) :

    response = redirect('/static/images/AA-41.jpg/')
    
    return response



def sheet_qp_93(request) :

    response = redirect('/static/images/QP-93.jpg/')
    
    return response



def sheet_qp_94(request) :

    response = redirect('/static/images/QP-94.jpg/')
    
    return response



def sheet_qp_95(request) :

    response = redirect('/static/images/QP-95.jpg/')
    
    return response



def sheet_fm_72(request) :

    response = redirect('/static/images/FM-72.jpg/')
    
    return response



def sheet_ab_84(request) :

    response = redirect('/static/images/AA-41.jpg/')
    
    return response



def sheet_fm_76(request) :

    response = redirect('/static/images/FM-76.jpg/')
    
    return response



def sheet_fm_71(request) :

    response = redirect('/static/images/FM-71.jpg/')
    
    return response



def sheet_fm_74(request) :

    response = redirect('/static/images/FM-74.jpg/')
    
    return response



def sheet_fm_75(request) :

    response = redirect('/static/images/FM-75.jpg/')
    
    return response



def sheet_fm_73(request) :

    response = redirect('/static/images/FM-73.jpg/')
    
    return response



def sheet_aa_43(request) :

    response = redirect('/static/images/AA-43.jpg/')
    
    return response



def sheet_aa_41(request) :

    response = redirect('/static/images/AA-41.jpg/')
    
    return response



def sheet_ml_805(request) :

    response = redirect('/static/images/ML-805.jpg/')
    
    return response



def sheet_ml_807(request) :

    response = redirect('/static/images/ML-807.jpg/')
    
    return response



def sheet_ml_806(request) :

    response = redirect('/static/images/ML-806.jpg/')
    
    return response



def sheet_ml_804(request) :

    response = redirect('/static/images/ML-804.jp/')
    
    return response



def sheet_mv_46(request) :

    response = redirect('/static/images/MV-46.jpg/')
    
    return response



def sheet_mv_45(request) :

    response = redirect('/static/images/MV-45.jpg/')
    
    return response



def sheet_wc_817(request) :

    response = redirect('/static/images/WC-817.jpg/')
    
    return response



def sheet_wc_815(request) :

    response = redirect('/static/images/WC-815.jpg')
    
    return response



def sheet_wc_816(request) :

    response = redirect('/static/images/WC-816.jpg/')
    
    return response



def sheet_fp_810(request) :

    response = redirect('/static/images/FP-810.jpg/')
    
    return response



def sheet_fm_74(request) :

    response = redirect('/static/images/FM-74.jpg/')
    
    return response



def sheet_fm_75(request) :

    response = redirect('/static/images/FM-75.jpg/')
    
    return response



def sheet_fm_73(request) :

    response = redirect('/static/images/FM-73.jpg/')
    
    return response



def sheet_aa_43(request) :

    response = redirect('/static/images/AA-43.jpg/')
    
    return response



def sheet_aa_41(request) :

    response = redirect('/static/images/AA-41.jpg/')
    
    return response



def sheet_ml_805(request) :

    response = redirect('/static/images/ML-805.jpg/')
    
    return response



def sheet_ml_807(request) :

    response = redirect('/static/images/ML-807.jpg/')
    
    return response



def sheet_ml_806(request) :

    response = redirect('/static/images/ML-806.jpg/')
    
    return response



def sheet_ml_804(request) :

    response = redirect('/static/images/ML-804.jp/')
    
    return response



def sheet_mv_46(request) :

    response = redirect('/static/images/MV-46.jpg/')
    
    return response



def sheet_mv_45(request) :

    response = redirect('/static/images/MV-45.jpg/')
    
    return response



def sheet_wc_817(request) :

    response = redirect('/static/images/WC-817.jpg/')
    
    return response



def sheet_wc_815(request) :

    response = redirect('/static/images/WC-815.jpg')
    
    return response



def sheet_wc_816(request) :

    response = redirect('/static/images/WC-816.jpg/')
    
    return response



def sheet_fp_810(request) :

    response = redirect('/static/images/FP-810.jpg/')
    
    return response



def sheet_fp_812(request) :

    response = redirect('/static/images/FP-812.jpg/')
    
    return response



def sheet_fp_813(request) :

    response = redirect('/static/images/FP-813.jpg/')
    
    return response



def sheet_fp_811(request) :

    response = redirect('/static/images/FP-811.jpg/')
    
    return response



def sheet_ss_89(request) :

    response = redirect('/static/images/SS-89.jpg/')
    
    return response



def sheet_bo_06(request) :

    response = redirect('/static/images/BO-06.jpg/')
    
    return response



def sheet_bo_07(request) :

    response = redirect('/static/images/BO-07.jpg/')
    
    return response



def sheet_bo_05(request) :

    response = redirect('/static/images/BO-05.jpg/')
    
    return response



def sheet_lc_77(request) :

    response = redirect('/static/images/LC-77.jpg/')
    
    return response



def sheet_lc_78(request) :

    response = redirect('/static/images/LC-78.jpg/')
    
    return response



def sheet_lc_79(request) :

    response = redirect('/static/images/LC-79.jpg/')
    
    return response



def sheet_lc_80(request) :

    response = redirect('/static/images/LC-80.jpg/')
    
    return response



def sheet_ic_801(request) :

    response = redirect('/static/images/IC-801.jpg/')
    
    return response



def sheet_ic_803(request) :

    response = redirect('/static/images/IC-803.jpg')
    
    return response



def sheet_ic_802(request) :

    response = redirect('/static/images/IC-802.jpg/')
    
    return response



def sheet_ra_01(request) :

    response = redirect('/static/images/RA-01.jpg/')
    
    return response

# ###########################


def sheet_ra_02(request) :

    response = redirect('/static/images/RA-02.jpg/')
    
    return response



def sheet_gg_52(request) :

    response = redirect('/static/images/GG-52.jpg/')
    
    return response



def sheet_gg_53(request) :

    response = redirect('/static/images/GG-53.jpg/')
    
    return response



def sheet_gg_54(request) :

    response = redirect('/static/images/GG-54.jpg/')
    
    return response



def sheet_gg_51(request) :

    response = redirect('/static/images/GG-51.jpg/')
    
    return response



def sheet_wa_58(request) :

    response = redirect('/static/images/WA-58.jpg/')
    
    return response



def sheet_wa_59(request) :

    response = redirect('/static/images/WA-59.jpg/')
    
    return response



def sheet_wa_60(request) :

    response = redirect('/static/images/WA-60.jpg/')
    
    return response



def sheet_wa_57(request) :

    response = redirect('/static/images/WA-57.jpg/')
    
    return response



def sheet_rp_61(request) :

    response = redirect('/static/images/RP-61.jpg/')
    
    return response



def sheet_rp_63(request) :

    response = redirect('/static/images/RP-63.jpg/')
    
    return response



def sheet_rp_65(request) :

    response = redirect('/static/images/RP-65.jpg/')
    
    return response



def sheet_rp_64(request) :

    response = redirect('/static/images/RP-64.jpg/')
    
    return response



def sheet_rp_62(request) :

    response = redirect('/static/images/RP-62.jpg/')
    
    return response



def sheet_ss_88(request) :

    response = redirect('/static/images/SS-88.jpg')
    
    return response



def sheet_sa_33(request) :

    response = redirect('/static/images/SA-33.jpg/')
    
    return response



def sheet_sa_31(request) :

    response = redirect('/static/images/SA-31.jpg/')
    
    return response



def sheet_sa_32(request) :

    response = redirect('/static/images/SA-32.jpg/')
    
    return response



def sheet_ct_11(request) :

    response = redirect('/static/images/CT-11.jpg/')
    
    return response



def sheet_ct_12(request) :

    response = redirect('/static/images/CT-12.jpg/')
    
    return response



def sheet_ra_04(request) :

    response = redirect('/static/images/RA-04.jpg/')
    
    return response



def sheet_nm_15(request) :

    response = redirect('/static/images/NM-15.jpg/')
    
    return response



def sheet_nm_16(request) :

    response = redirect('/static/images/NM-16.jpg/')
    
    return response



def sheet_nm_19(request) :

    response = redirect('/static/images/NM-19.jpg/')
    
    return response



def sheet_nm_18(request) :

    response = redirect('/static/images/NM-18.jpg/')
    
    return response



def sheet_gr_14(request) :

    response = redirect('/static/images/GR-14.jpg/')
    
    return response



def sheet_gr_13(request) :

    response = redirect('/static/images/GR-13.jpg/')
    
    return response






