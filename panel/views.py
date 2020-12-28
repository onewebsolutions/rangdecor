import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from panel.models import Page_Handler, Looper_Section, Looper_Component, Informative_Section
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from ipware import get_client_ip



############################## Panel #############################

def panel(request) :

    return render(request, 'panel.html')




############################ Page Handler #######################

def page_handler(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        page_name = request.POST.get('page_name', '')
        page_info = request.POST.get('page_info', '')
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        page_handler = Page_Handler.objects.all()

        for ph in page_handler :
            if ph.page_name == page_name :
                return HttpResponse('Two pages can not have same name, it will create confusion in long run. If you still want to keep it same then use numarator to uniquely identify each ! ')


        obj = Page_Handler(index=index, page_name=page_name, page_info=page_info, meta_title=meta_title, meta_description=meta_description)
        obj.save()

        return redirect('page_handler')


    page = Page_Handler.objects.all()


    return render(request, 'page_handler.html', {
        'page': page,
    })



def page_handler_edit(request, page_name_w) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        page_name = request.POST.get('page_name', '')
        page_info = request.POST.get('page_info', '')        
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        page_handler = Page_Handler.objects.all().exclude(page_name=page_name_w)

        for ph in page_handler :
            if ph.page_name == page_name :
                return HttpResponse('Two pages can not have same name, it will create confusion in long run. If you still want to keep it same then use numarator to uniquely identify each ! ')



        obj = Page_Handler.objects.get(page_name=page_name_w)

        obj.index = index
        obj.page_name = page_name
        obj.page_info = page_info
        obj.meta_title = meta_title
        obj.meta_description = meta_description

        obj.save()

        return redirect('page_handler')


    page = Page_Handler.objects.all()

    page = Page_Handler.objects.get(page_name=page_name_w)


    return render(request, 'page_handler_edit.html', {
        'page': page,
    })



def page_delete(request, page_name_w) :

    obj = Page_Handler.objects.get(page_name=page_name_w)
    obj.delete()

    return redirect('page_handler')




    
################################### Looper Section ################################


def looper_section(request) :

    page = Page_Handler.objects.all()
    looper_section = Looper_Section.objects.all()

    # msg = "Hey there, we are just testing the message feature of django !"
    # messages.success(request, msg)

    return render(request, 'looper_section.html', {
        'page': page,
        'looper_section': looper_section,
    })



def looper_section_add(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        page = request.POST.get('page', '')
        name = request.POST.get('name', '')

        looper_section = Looper_Section.objects.all()

        for ls in looper_section :
            if ls.name == name :
                return HttpResponse('Two sections can not have same name, it will create confusion in long run. If you still want to keep it same then add page name before it followed by underscore or use numarator to uniquely identify each ! ')


        try:
            obj_page = Page_Handler.objects.get(page_name=page)
        except Page_Handler.DoesNotExist:
            obj_page = None

        if obj_page != None :

            obj = Looper_Section(fk=obj_page, page_name=obj_page.page_name, index=index, name=name)
            obj.save()

            msg = "Looper Section has been successfully added to list !"
            messages.success(request, msg)

            return redirect('looper_section')

        else :

            return HttpResponse("Not valid Section Name")



def looper_section_delete(request, loop_sec_pk) :

    try:
        looper_section = Looper_Section.objects.get(pk=loop_sec_pk)
    except Looper_Section.DoesNotExist:
        looper_section = None

    if looper_section != None :

        looper_section.delete()

        msg = "Looper Section has been successfully deleted !"
        messages.success(request, msg)

        return redirect('looper_section')

    else :

        return HttpResponse("Something happened while deleting the Looper Sectiion Object ! ")



def looper_section_edit(request, loop_sec_pk) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        page = request.POST.get('page', '')
        name = request.POST.get('name', '')

        try:
            obj_page = Page_Handler.objects.get(page_name=page)
        except Page_Handler.DoesNotExist:
            obj_page = None

        if obj_page != None :

            try:
                obj_looper_section = Looper_Section.objects.get(pk=loop_sec_pk)
            except Looper_Section.DoesNotExist:
                obj_looper_section = None

            if obj_looper_section != None :

                obj_looper_section.index = index
                obj_looper_section.page_name = page
                obj_looper_section.name = name

                if page != obj_page.page_name :

                    obj_looper_section.fk = obj_page

                obj_looper_section.save()

                msg = "Changes made to Looper Section has been successfully updated !"
                messages.success(request, msg)

                return redirect('looper_section')

            else :
                return HttpResponse("Looper Section could not be found !")

        else :

            return HttpResponse("Page Handler could not be found !")



    try:
        looper_section = Looper_Section.objects.get(pk=loop_sec_pk)
    except Looper_Section.DoesNotExist:
        looper_section = None

    if looper_section != None :
        
        page = Page_Handler.objects.all()

        return render(request, 'looper_section_edit.html', {
            'looper_section': looper_section,
            'page': page,
        })

    else :

        return HttpResponse('Error : something happened while editing the looper section object ! ')




################################## Looper Component ###############################


def looper_component(request, loop_sec_name_w) :

    try:
        looper_section = Looper_Section.objects.get(name=loop_sec_name_w)
    except Looper_Section.DoesNotExist:
        looper_section = None

    if looper_section != None :

        looper_component = Looper_Component.objects.filter(fk=looper_section)
        
        return render(request, 'looper_component.html', {
            'looper_section': looper_section,
            'looper_component': looper_component,
        })

    else :

        return HttpResponse("No Looper Section found !")



def looper_component_add(request, loop_sec_name_w) :

    if request.method == 'POST' :

        try:
            looper_section = Looper_Section.objects.get(name=loop_sec_name_w)
        except Looper_Section.DoesNotExist:
            looper_section = None

        if looper_section != None :

            index = request.POST.get('index', '')
            section_name = request.POST.get('section_name', '')
            name = request.POST.get('name', '')
            title = request.POST.get('title', '')
            intro = request.POST.get('intro', '')
            detail = request.POST.get('detail', '')
            main_image = request.FILES.get('main_image', None)
            second_image = request.FILES.get('second_image', None)
            third_image = request.FILES.get('third_image', None)
            bg_image = request.FILES.get('bg_image', None)
            side = request.POST.get('side', '')

            page_name = looper_section.page_name

            obj = Looper_Component(

                fk = looper_section,
                page_name = page_name,
                section_name = section_name,
                name = name,
                index = index,
                title = title,
                intro = intro,
                detail = detail,
                main_image = main_image,
                second_image = second_image,
                third_image = third_image,
                bg_image = bg_image,
                side = side,

            )

            obj.save()

            return redirect('looper_component', loop_sec_name_w)

        else :

            return HttpResponse("Error : Something heppened while retrieving looper section object ! ")

    return HttpResponse("hey")



def looper_component_edit(request, loop_sec_name_w, loop_comp_pk) :

    if request.method == 'POST' :

        try:
            looper_component = Looper_Component.objects.get(pk=loop_comp_pk)
        except Looper_Component.DoesNotExist:
            looper_component = None

        if looper_component != None :

            index = request.POST.get('index', '')
            section_name = request.POST.get('section_name', '')
            name = request.POST.get('name', '')
            title = request.POST.get('title', '')
            intro = request.POST.get('intro', '')
            detail = request.POST.get('detail', '')
            main_image = request.FILES.get('main_image', None)
            second_image = request.FILES.get('second_image', None)
            third_image = request.FILES.get('third_image', None)
            bg_image = request.FILES.get('bg_image', None)
            side = request.POST.get('side', '')


            if main_image != None :
                if looper_component.main_image :
                    default_storage.delete(looper_component.main_image.path)
                looper_component.main_image = main_image
            if second_image != None :
                if looper_component.second_image :
                    default_storage.delete(looper_component.second_image.path)
                looper_component.second_image = second_image
            if third_image != None :
                if looper_component.third_image :
                    default_storage.delete(looper_component.third_image.path)
                looper_component.third_image = third_image
            if bg_image != None :
                if looper_component.bg_image :
                    default_storage.delete(looper_component.bg_image.path)
                looper_component.bg_image = bg_image

            looper_component.index = index
            looper_component.section_name = section_name
            looper_component.name = name
            looper_component.title = title
            looper_component.intro = intro
            looper_component.detail = detail
            looper_component.side = side

            looper_component.save()

            msg = "Changes made to Looper Component has been successfully applied !"
            messages.success(request, msg)

            return redirect('looper_component', loop_sec_name_w)

        else :

            return HttpResponse("Could not find Looper Object with given PK !")

    try:
        looper_component = Looper_Component.objects.get(pk=loop_comp_pk)
    except Looper_Component.DoesNotExist:
        looper_component = None

    if looper_component != None :

        try:
            looper_section = Looper_Section.objects.get(name=loop_sec_name_w)
        except Looper_Section.DoesNotExist:
            looper_section = None

        if looper_section != None :

            return render(request, 'looper_component_edit.html', {
                'looper_component': looper_component,
                'looper_section': looper_section,
            })

        else :
            return HttpResponse("Looper Section Not Found !")

    else :
        return HttpResponse("Looper Component Not Found !")



def looper_component_delete(request, loop_sec_name_w, loop_comp_pk) :

    try:
        looper_component = Looper_Component.objects.get(pk=loop_comp_pk)
        looper_component.delete()

        msg = "Looper Component Deleted !"
        messages.success(request, msg)

        return redirect('looper_component', loop_sec_name_w)

    except :

        return redirect('looper_component', loop_sec_name_w)

    return HttpResponse("You are somewhere in-between looper component function's success and failure")



def remove_image_looper_component(request, loop_comp_pk, img_path, img_name) :

    if img_name == "main_image" :

        looper = Looper_Component.objects.get(pk=loop_comp_pk)

        section_name = looper.fk.name

        default_storage.delete(img_path)
        looper.main_image = None
        looper.save()

        msg = "Looper Component Updated !"
        messages.success(request, msg)

        return redirect('looper_component', section_name)

    elif img_name == "second_image" :

        looper = Looper_Component.objects.get(pk=loop_comp_pk)

        section_name = looper.fk.name

        default_storage.delete(img_path)
        looper.second_image = None
        looper.save()

        msg = "Looper Component Updated !"
        messages.success(request, msg)

        return redirect('looper_component', section_name)

    elif img_name == "third_image" :

        looper = Looper_Component.objects.get(pk=loop_comp_pk)

        section_name = looper.fk.name

        default_storage.delete(img_path)
        looper.third_image = None
        looper.save()

        msg = "Looper Component Updated !"
        messages.success(request, msg)

        return redirect('looper_component', section_name)

    elif img_name == "bg_image" :

        looper = Looper_Component.objects.get(pk=loop_comp_pk)

        section_name = looper.fk.name

        default_storage.delete(img_path)
        looper.bg_image = None
        looper.save()

        msg = "Looper Component Updated !"
        messages.success(request, msg)

        return redirect('looper_component', section_name)

    else :

        return HttpResponse("Deletion Failed !")






################################## Informative Section ###############################


def informative_section(request) :

    informative = Informative_Section.objects.all()

    page =  Page_Handler.objects.all()

    return render(request, 'informative_section.html', {
        'informative': informative,
        'page' : page,
    })



def informative_section_add(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        page_name = request.POST.get('page_name', '')
        section_name = request.POST.get('section_name', '')
        sub_section_name = request.POST.get('sub_section_name', '')
        title = request.POST.get('title', '')
        intro = request.POST.get('intro', '')
        detail = request.POST.get('detail', '')
        main_image = request.FILES.get('main_image', None)
        second_image = request.FILES.get('second_image', None)
        third_image = request.FILES.get('third_image', None)
        bg_image = request.FILES.get('bg_image', None)
        side = request.POST.get('side', '')

        obj = Informative_Section(

            index = index,
            page_name = page_name,
            section_name = section_name,
            sub_section_name = sub_section_name,
            title = title,
            intro = intro,
            detail = detail,
            main_image = main_image,
            second_image = second_image,
            third_image = third_image,
            bg_image = bg_image,
            side = side,

        )

        obj.save()

        msg = "Informative component added successfully !"
        messages.success(request, msg)

        return redirect('informative_section')



def informative_section_edit(request, pk) :

    if request.method == 'POST' :

        try:
            informative = Informative_Section.objects.get(pk=pk)
        except Informative_Section.DoesNotExist:
            informative = None  

        if informative != None :

            index = request.POST.get('index', '')
            page_name = request.POST.get('page_name', '')
            section_name = request.POST.get('section_name', '')
            sub_section_name = request.POST.get('sub_section_name', '')
            title = request.POST.get('title', '')
            intro = request.POST.get('intro', '')
            detail = request.POST.get('detail', '')
            main_image = request.FILES.get('main_image', None)
            second_image = request.FILES.get('second_image', None)
            third_image = request.FILES.get('third_image', None)
            bg_image = request.FILES.get('bg_image', None)
            side = request.POST.get('side', '')


            if main_image != None :
                if informative.main_image :
                    default_storage.delete(informative.main_image.path)
                informative.main_image = main_image
            if second_image != None :
                if informative.second_image :
                    default_storage.delete(informative.second_image.path)
                informative.second_image = second_image
            if third_image != None :
                if informative.third_image :
                    default_storage.delete(informative.third_image.path)
                informative.third_image = third_image
            if bg_image != None :
                if informative.bg_image :
                    default_storage.delete(informative.bg_image.path)
                informative.bg_image = bg_image

            informative.index = index
            informative.page_name = page_name
            informative.section_name = section_name
            informative.sub_section_name = sub_section_name
            informative.title = title
            informative.intro = intro
            informative.detail = detail
            informative.side = side

            informative.save()

            msg = "Updated made to Informative Section are applied successfully !"
            messages.success(request, msg)

            return redirect('informative_section')


        else :
            HttpResponse("Object not found while updating the Informative Section !")



    try:
        informative = Informative_Section.objects.get(pk=pk)
    except Informative_Section.DoesNotExist:
        informative = None    

    page = Page_Handler.objects.all()

    if informative != None :
        return render(request, 'informative_section_edit.html', {
            'informative': informative,
            'page': page,
        })
        
    else :
        HttpResponse("Object not found !")



def remove_image(request, img_name, img_path, pk) :

    if img_name == "main_image" :

        informative = Informative_Section.objects.get(pk=pk)

        default_storage.delete(img_path)
        informative.main_image = None
        informative.save()

        msg = "Image removed successfully !"
        messages.success(request, msg)

        return redirect('informative_section')

    if img_name == "second_image" :

        informative = Informative_Section.objects.get(pk=pk)

        default_storage.delete(img_path)
        informative.second_image = None
        informative.save()

        msg = "Image removed successfully !"
        messages.success(request, msg)

        return redirect('informative_section')

    if img_name == "third_image" :

        informative = Informative_Section.objects.get(pk=pk)

        default_storage.delete(img_path)
        informative.third_image = None
        informative.save()

        msg = "Image removed successfully !"
        messages.success(request, msg)

        return redirect('informative_section')

    if img_name == "bg_image" :

        informative = Informative_Section.objects.get(pk=pk)

        default_storage.delete(img_path)
        informative.bg_image = None
        informative.save()

        msg = "Image removed successfully !"
        messages.success(request, msg)

        return redirect('informative_section')

    else :

        return HttpResponse("Deletion failed ! ")



def informative_section_delete(request, pk) :

    try:
        informative = Informative_Section.objects.get(pk=pk)
    except Informative_Section.DoesNotExist:
        informative = None    


    if informative != None :

        informative.delete()

        msg = "Informative Section deleted !"
        messages.success(request, msg)

        return redirect('informative_section')

    else :

        return HttpResponse('Object not found !')




