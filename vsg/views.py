from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from product.models import Product
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from django.contrib import messages
from product.models import Product, Sheet
from django.db.models import Q
from itertools import chain
from vsg.models import VSG
from django.core.files.storage import default_storage



def vsg(request, vsg_area) :

    try :
        vsg = VSG.objects.get(area_id=vsg_area)
    except :
        vsg = None

    if vsg != None :

        product = Product.objects.all()

        sheet = Sheet.objects.none()

        vsgs = VSG.objects.all()
        

        for p in product :
            q = Sheet.objects.filter(fk=p).order_by('-index')
            sheet = sheet | q


        return render(request, 'vsg.html', {
            'vsg': vsg,
            'vsgs': vsgs,
            'sheet': sheet,
            'product': product,
        })


    else :

        return HttpResponse("Visual Gallery area not found ! ")



def vsg_back(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        area = request.POST.get('area', '')
        area_id = request.POST.get('area_id', '')
        detail = request.POST.get('detail', '')
        main_image = request.FILES.get('main_image', None)
        is_show = request.POST.get('is_show', '')
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        vsg_ = VSG.objects.all()

        show_count = 0

        for vsg_ in vsg_ :
            if vsg_.area_id == area_id :
                return HttpResponse("Area_id can not be same !")
            
            if vsg_.is_show == 'yes'  :
                show_count += 1
        
        if is_show != '' :
            if show_count > 0 :
                return HttpResponse("Can not list more than one Area on Menu!")
            

        vsg = VSG(
            index = index,
            area = area,
            area_id = area_id,
            detail = detail,
            main_image = main_image,
            is_show = is_show,
            meta_title = meta_title,
            meta_description = meta_description,
        )

        vsg.save()

        msg = "Visual Gallery Area has been added !"
        messages.success(request, msg)


        return redirect('vsg_back')  



    vsg = VSG.objects.all()

    return render(request, 'vsg_back.html', {
        'vsg': vsg,
    })



def vsg_back_edit(request, vsg_pk) :

    if request.method == 'POST' :

        try :
            vsg = VSG.objects.get(pk=vsg_pk)
        except :
            vsg = None

        if vsg != None :


            index = request.POST.get('index', '')
            detail = request.POST.get('detail', '')
            area = request.POST.get('area', '')
            area_id = request.POST.get('area_id', '')
            main_image = request.FILES.get('main_image', None)
            is_show = request.POST.get('is_show', '')
            meta_title = request.POST.get('meta_title', '')
            meta_description = request.POST.get('meta_description', '')

            vsg_ = VSG.objects.all().exclude(pk=vsg_pk)

            show_count = 0

            for vsg_ in vsg_ :
                if vsg_.area_id == area_id :
                    return HttpResponse("Area_id can not be same !")

                if vsg_.is_show == 'yes'  :
                    show_count += 1

            if is_show != '' :
                if show_count > 0 :
                    return HttpResponse("Can not list more than one Area on Menu!")


            if main_image != None :
                if vsg.main_image :
                    default_storage.delete(vsg.main_image.path)
                vsg.main_image = main_image

            vsg.index = index
            vsg.area = area
            vsg.area_id = area_id
            vsg.detail = detail
            vsg.is_show = is_show
            vsg.meta_title = meta_title
            vsg.meta_description = meta_description

            vsg.save()

            msg = "Edits made to Visual Gallery has been executed successfully !"
            messages.success(request, msg)

            return redirect('vsg_back')

        else :

            return HttpResponse("Visual Gallery Object not found !")


    try :
        vsg = VSG.objects.get(pk=vsg_pk)
    except :
        vsg = None

        print(vsg)
        print("-----------------")

    if vsg != None :

        return render(request, 'vsg_back_edit.html', {
            'vsg': vsg,
        })

    else :

        return HttpResponse("Visual Gallery object not found !")



def vsg_back_delete(request, vsg_pk) :

    try :
        vsg = VSG.objects.get(pk=vsg_pk)
    except :
        vsg = None

    if vsg != None :

        vsg.delete()

        msg = "Deletion completed !"
        messages.success(request, msg)

        return redirect('vsg_back')

    else :

        return HttpResponse("Visual Gallery area not found !")















