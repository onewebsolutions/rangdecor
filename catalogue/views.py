from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from panel.models import  Page_Handler, Informative_Section, Looper_Component, Looper_Section
from product.models import Product, Sheet
from catalogue.models import Catalogue, Catalogue_Page
from django.contrib import messages
from django.core.files.storage import default_storage


def catalogue_back(request) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == "POST" :

        index = request.POST.get('index', '')
        name = request.POST.get('name', '')
        name_id = request.POST.get('name_id', '')
        page_first = request.POST.get('page_first', '')
        page_second = request.POST.get('page_second', '')
        page_height = request.POST.get('page_height', '')
        page_width = request.POST.get('page_width', '')
        main_image_1 = request.FILES.get('main_image_1', None)
        main_image_2 = request.FILES.get('main_image_2', None)
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        if index.isupper() or index.islower() or page_first.isupper() or page_first.islower() or page_second.isupper() or page_second.islower() or page_height.isupper() or page_height.islower() or page_width.isupper() or page_width.islower() :
            return HttpResponse("Number field can only accept numbers!")

        obj = Catalogue(
            index = index,
            name = name,
            name_id = name_id,
            page_first = page_first,
            page_second = page_second,
            page_height = page_height,
            page_width = page_width,
            main_image_1 = main_image_1,
            main_image_2 = main_image_2,
            meta_title = meta_title,
            meta_description = meta_description,
        )

        obj.save()

        msg = "New catalogue has been added successfully, go ahead and cosider adding some full-sheets to it!"
        messages.success(request, msg)


        return redirect('catalogue_back')


    catalogue = Catalogue.objects.all()

    return render(request, 'catalogue_back.html', {
        'catalogue': catalogue,
    })



def catalogue_back_edit(request, cata_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == 'POST' :

        try:
            catalogue = Catalogue.objects.get(pk=cata_pk)
        except Catalogue.DoesNotExist:
            catalogue = None

        if catalogue != None :

            index = request.POST.get('index', '')
            name = request.POST.get('name', '')
            name_id = request.POST.get('name_id', '')        
            page_first = request.POST.get('page_first', '')
            page_second = request.POST.get('page_second', '')        
            page_height = request.POST.get('page_height', '')
            page_width = request.POST.get('page_width', '')
            main_image_1 = request.FILES.get('main_image_1', None)
            main_image_2 = request.FILES.get('main_image_2', None)
            meta_title = request.POST.get('meta_title', '')
            meta_description = request.POST.get('meta_description', '')

            if index.isupper() or index.islower() or page_first.isupper() or page_first.islower() or page_second.isupper() or page_second.islower() or page_height.isupper() or page_height.islower() or page_width.isupper() or page_width.islower() :
                return HttpResponse("Number field can only accept numbers!")

            if main_image_1 != None :
                if catalogue.main_image_1 :
                    default_storage.delete(catalogue.main_image_1.path)
                catalogue.main_image_1 = main_image_1
                
            if main_image_2 != None :
                if catalogue.main_image_2 :
                    default_storage.delete(catalogue.main_image_2.path)
                catalogue.main_image_2 = main_image_2

            
            catalogue.index = index
            catalogue.name = name
            catalogue.name_id = name_id
            catalogue.page_first = page_first
            catalogue.page_second = page_second
            catalogue.page_height = page_height
            catalogue.page_width = page_width
            catalogue.meta_title = meta_title
            catalogue.meta_description = meta_description

            catalogue.save()

            msg = "Catalogue Information has been updated according to recent changes !"
            messages.success(request, msg)

            return redirect('catalogue_back')

        else :
            return HttpResponse("Catalogue not found, try going back and refreshing the page !")




    try:
        catalogue = Catalogue.objects.get(pk=cata_pk)
    except Catalogue.DoesNotExist:
        catalogue = None

    if catalogue != None :

        return render(request, 'catalogue_back_edit.html', {
            'catalogue': catalogue,
        })

    else :
        return HttpResponse("Catalogue not found, try going back and refreshing the page !")



def catalogue_back_page(request, cata_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == "POST" :

        try:
            catalogue = Catalogue.objects.get(pk=cata_pk)
        except Catalogue.DoesNotExist:
            catalogue = None

        if catalogue != None :

            index = request.POST.get('index', '')
            page_first = request.POST.get('page_first', '')
            main_image_1 = request.FILES.get('main_image_1', None)
            page_second = request.POST.get('page_second', '')
            main_image_2 = request.FILES.get('main_image_2', None)

            if index.isupper() or index.islower() or page_first.isupper() or page_first.islower() or page_second.isupper() or page_second.islower() :
                return HttpResponse("Number field can only accept numbers!")

            obj = Catalogue_Page(
                fk = catalogue,
                index = index,
                page_first = page_first,
                page_second = page_second,
                main_image_1 = main_image_1,
                main_image_2 = main_image_2,
            )

            obj.save()

            msg = "New page has been added to catalogue !"
            messages.success(request, msg)

            return redirect('catalogue_back_page', cata_pk)

        else :

            return HttpResponse("Can not add new page to catalogue due to some technical error ! Try again later !")



    try:
        catalogue = Catalogue.objects.get(pk=cata_pk)
    except Catalogue.DoesNotExist:
        catalogue = None

    if catalogue != None :

        catalogue_page = Catalogue_Page.objects.all()

        return render(request, 'catalogue_back_page.html', {
            'catalogue': catalogue,
            'catalogue_page':catalogue_page,
        })

    else :
        return HttpResponse("Catalogue not found, try going back and refreshing the page !")



def catalogue_back_page_edit(request, cata_pk, page_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == 'POST' :

        try:
            catalogue_page = Catalogue_Page.objects.get(pk=page_pk)
        except Catalogue_Page.DoesNotExist:
            catalogue_page = None

        if catalogue_page != None :

            index = request.POST.get('index', '')
            page_first = request.POST.get('page_first', '')
            main_image_1 = request.FILES.get('main_image_1', None)
            page_second = request.POST.get('page_second', '')
            main_image_2 = request.FILES.get('main_image_2', None)

            if index.isupper() or index.islower() or page_first.isupper() or page_first.islower() or page_second.isupper() or page_second.islower() :
                return HttpResponse("Number field can only accept numbers!")

            if main_image_1 != None :
                if catalogue_page.main_image_1 :
                    default_storage.delete(catalogue_page.main_image_1.path)
                catalogue_page.main_image_1 = main_image_1

            if main_image_2 != None :
                if catalogue_page.main_image_2 :
                    default_storage.delete(catalogue_page.main_image_2.path)
                catalogue_page.main_image_2 = main_image_2

            catalogue_page.index = index
            catalogue_page.page_first = page_first
            catalogue_page.page_second = page_second

            catalogue_page.save()


            msg = "Updated the Page Info !"
            messages.success(request, msg)

            return redirect('catalogue_back_page', cata_pk)
        else :
            return HttpResponse("Somehting went wrong while editing the catalogue page !")

    try:
        catalogue_page = Catalogue_Page.objects.get(pk=page_pk)
    except Catalogue_Page.DoesNotExist:
        catalogue_page = None

    if catalogue_page != None :

        try:
            catalogue = Catalogue.objects.get(pk=cata_pk)
        except Catalogue.DoesNotExist:
            catalogue = None

        if catalogue != None :

            return render(request, 'catalogue_back_page_edit.html', {
                'catalogue': catalogue,
                'catalogue_page': catalogue_page,
            })

        else :
            return HttpResponse("Catalogue object not foung !")

    else :
        return HttpResponse("Catalogue object not found !")



def catalogue_back_page_delete(request, cata_pk, page_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    try:
        catalogue_page = Catalogue_Page.objects.get(pk=page_pk)
    except Catalogue_Page.DoesNotExist:
        catalogue_page = None

    if catalogue_page != None :

        catalogue_page.delete()

        msg = "Page has been removed from the catalogue !"
        messages.success(request, msg)

        return redirect('catalogue_back_page', cata_pk)

    else :
        return HttpResponse("Error happened while deleting the product page, try deleting it again!")




