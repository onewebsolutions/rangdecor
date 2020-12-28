import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import default_storage
from product.models import Product, Sheet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages





def product_back(request) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    product = Product.objects.all()

    return render(request, 'product_back.html', {
        'product' : product,
    })



def product_add(request) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    if request.method == 'POST' :

        index = request.POST.get('index', '')
        product_name = request.POST.get('product_name', '')
        title = request.POST.get('title', '')
        intro = request.POST.get('intro', '')
        detail = request.POST.get('detail', '')
        main_image = request.FILES.get('main_image', None)
        is_vsg = request.FILES.get('is_vsg', '')
        is_tab = request.FILES.get('is_tab', '')
        is_paginate = request.FILES.get('is_paginate', '')
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        product = Product(
            index = index,
            product_name = product_name,
            title = title,
            intro = intro,
            detail = detail,
            main_image = main_image,
            is_vsg = is_vsg,
            is_tab = is_tab,
            is_paginate = is_paginate,
            meta_title = meta_title,
            meta_description = meta_description,
        )

        product.save()

        msg = "Product is added !"
        messages.success(request, msg)

        return redirect('product_back')

    else : 

        return HttpResponse('This is Product Add function so only POST requests are acceptable here, recheck your code and confirm that flow is proper !')



def product_edit(request, product_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    if request.method == 'POST' :

        index = request.POST.get('index', '')
        product_name = request.POST.get('product_name', '')
        title = request.POST.get('title', '')
        intro = request.POST.get('intro', '')
        detail = request.POST.get('detail', '')
        is_vsg = request.POST.get('is_vsg', '')
        is_tab = request.POST.get('is_tab', '')
        is_paginate = request.POST.get('is_paginate', '')
        
        main_image = request.FILES.get('main_image', None)

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        
        try:
            product = Product.objects.get(pk=product_pk)
        except Product.DoesNotExist:
            product = None    

        if product != None :

            product.index = index
            product.product_name = product_name
            product.meta_title = meta_title
            product.meta_description = meta_description
            product.title = title
            product.intro = intro
            product.detail = detail
            product.is_vsg = is_vsg
            product.is_tab = is_tab
            product.is_paginate = is_paginate

            if main_image != None :
                if product.main_image :
                    default_storage.delete(product.main_image.path)
                product.main_image = main_image


            product.save()

            msg = "Changes made to product have been applied successfully !"
            messages.success(request, msg)

        return redirect('product_back')


    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        product = None    

    if product != None :

        return render(request, 'product_edit.html', {
            'product': product,
        })

    else : 

        return HttpResponse('Object not found !')



def product_delete(request, product_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        product = None

    if product != None :

        if product.main_image :
            default_storage.delete(product.main_image.path)
        
        product.delete()

        msg = "Product is deleted !"
        messages.success(request, msg)

        return redirect('product_back')

    else :
        return HttpResponse("Something went wrong while deleting the Product object !")



def remove_image(request, product_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        product = None    

    if product != None :
            
        default_storage.delete(product.main_image.path)
        product.main_image = None

        product.save()

        msg = "Image has been removed !"
        messages.success(request, msg)

        return redirect('product_back')

    else :

        return HttpResponse("Product object not found, deletion failed ! ")



def sheet_back(request, product_pk) : 

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        product = None   

    if product != None :

        sheet = Sheet.objects.filter(fk=product)

        return render(request, 'sheet_back.html', {
            'product_pk': product_pk,
            'product': product,
            'sheet': sheet,
        })



    else :
        return HttpResponse('Product object not found !')



def sheet_add(request, product_pk) : 

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        product = None   

    if product != None :

        index = request.POST.get('index', '')
        number = request.POST.get('number', '')
        name = request.POST.get('name', '')
        main_finish = request.POST.get('main_finish', '')
        sub_finish = request.POST.get('sub_finish', '')
        main_image = request.FILES.get('main_image', None)

        sheet = Sheet(
            index = index,
            number = number,
            name = name,
            main_finish = main_finish,
            sub_finish = sub_finish,
            main_image = main_image,
            fk = product,
        )

        sheet.save()

        msg = "Sheet has been added to Product Page !"
        messages.success(request, msg)

        return redirect('sheet_back', product_pk)


    else :
        return HttpResponse('Product object not found !')


    
def sheet_edit(request, product_pk, sheet_pk) : 

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')


    if request.method == 'POST' :

        try:
            product = Product.objects.get(pk=product_pk)
        except Product.DoesNotExist:
            product = None    

        if product != None :

            try:
                sheet = Sheet.objects.get(pk=sheet_pk)
            except Sheet.DoesNotExist:
                sheet = None  

            if sheet != None :

                index = request.POST.get('index', '')
                number = request.POST.get('number', '')
                name = request.POST.get('name', '')
                main_finish = request.POST.get('main_finish', '')
                sub_finish = request.POST.get('sub_finish', '')
                main_image = request.FILES.get('main_image', None)

                if main_image != None :
                    if sheet.main_image :
                        default_storage.delete(sheet.main_image.path)
                    sheet.main_image = main_image

                sheet.index = index
                sheet.number = number
                sheet.name = name
                sheet.main_finish = main_finish
                sheet.sub_finish = sub_finish

                sheet.save()

                msg = "Updates made to the product sheet object are successfully commited !"
                messages.success(request, msg)

                return redirect('sheet_back', product_pk)

            else :
                return HttpResponse('Sheet object not found ! ')

        else :
            return HttpResponse('Product object not found !')


    try:
        product = Product.objects.get(pk=product_pk)
    except Product.DoesNotExist:
        product = None    

    if product != None :

        try:
            sheet = Sheet.objects.get(pk=sheet_pk)
        except Sheet.DoesNotExist:
            sheet = None  

        if sheet != None :

            return render(request, 'sheet_edit.html', {
                'product_pk': product_pk,
                'product': product,
                'sheet': sheet,
            })

        else :
            return HttpResponse('Sheet object not found ! ')
    
    else :
        return HttpResponse('Product object not found ! ')



def sheet_delete(request, product_pk, sheet_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')



    try:
        sheet = Sheet.objects.get(pk=sheet_pk)
    except Sheet.DoesNotExist:
        sheet = None  

    if sheet != None :

        sheet.delete()

        msg = ""

        return redirect('sheet_back', product_pk)

    else :
        return HttpResponse('Sheet object not found ! ')

























