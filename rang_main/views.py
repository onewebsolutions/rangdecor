from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from panel.models import  Page_Handler, Informative_Section, Looper_Component, Looper_Section
from product.models import Product, Sheet
from catalogue.models import Catalogue, Catalogue_Page
from contact.models import Contact_Us
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from vsg.models import VSG



def home(request) :

    # current_url = resolve(request.path_info).url_name
    # return render(request, 'index.html')

    try : 
        page_handler = Page_Handler.objects.get(page_name='home')
    except :
        return HttpResponse("Page Handler Error, About page not found !")

    gallery = Looper_Section.objects.filter(page_name='gallery')

    product_head = Product.objects.all()

    catalogue = Catalogue.objects.all()

    vsg = VSG.objects.all()

    # --------------------_ looper _---------------------- #

    try : 
        ls1 = Looper_Section.objects.get(name='home_landing_slider')
        lc1 = Looper_Component.objects.filter(fk=ls1).order_by('index')
    except :
        lc1 = None

    try : 
        ls2 = Looper_Section.objects.get(name='home_service')
        lc2 = Looper_Component.objects.filter(fk=ls2).order_by('index')
    except :
        lc2 = None

    try : 
        ls3 = Looper_Section.objects.get(name='home_counter')
        lc3 = Looper_Component.objects.filter(fk=ls3).order_by('index')
    except :
        lc3 = None

    try : 
        ls4 = Looper_Section.objects.get(name='home_brand')
        lc4 = Looper_Component.objects.filter(fk=ls4).order_by('index')
    except :
        lc4 = None


    # --------------------_ informative _---------------------- #

    try :
        is1 = Informative_Section.objects.get(section_name="home_introduction")
    except :
        is1 = None

    try :
        is2 = Informative_Section.objects.get(section_name="home_service")
    except :
        is2 = None

    try :
        is3 = Informative_Section.objects.get(section_name="home_counter")
    except :
        is3 = None

    try :
        is4 = Informative_Section.objects.get(section_name="home_counter")
    except :
        is4 = None



    return render(request, 'index.html', {
        'page_handler': page_handler,
        'product_head': product_head,
        'catalogue': catalogue,
        'gallery': gallery,
        'vsg': vsg,
        'lc1': lc1,
        'lc2': lc2,
        'lc3': lc3,
        'lc4': lc4,
        'is1': is1,
        'is2': is2,
        'is3': is3,
    })


def about(request) : 

    try : 
        page_handler = Page_Handler.objects.get(page_name='about')
    except :
        return HttpResponse("Page Handler Error, About page not found !")

    gallery = Looper_Section.objects.filter(page_name='gallery')

    product_head = Product.objects.all()

    catalogue = Catalogue.objects.all()

    vsg = VSG.objects.all()


    # --------------------_ looper _---------------------- #

    try : 
        ls1 = Looper_Section.objects.get(name='about_introduction')
        lc1 = Looper_Component.objects.filter(fk=ls1).order_by('index')
    except :
        lc1 = None

    try : 
        ls2 = Looper_Section.objects.get(name='about_brand')
        lc2 = Looper_Component.objects.filter(fk=ls2).order_by('index')
    except :
        lc2 = None

    try : 
        ls3 = Looper_Section.objects.get(name='about_feature')
        lc3 = Looper_Component.objects.filter(fk=ls3).order_by('index')
    except :
        lc3 = None

    try : 
        ls4 = Looper_Section.objects.get(name='about_application')
        lc4 = Looper_Component.objects.filter(fk=ls4).order_by('index')
    except :
        lc4 = None



    # --------------------_ informative _---------------------- #

    try :
        is1 = Informative_Section.objects.get(section_name="about_breadcrumb")
    except :
        is1 = None

    try :
        is2 = Informative_Section.objects.get(section_name="about_introduction")
    except :
        is2 = None


    

    return render(request, 'about.html', {
        'page_handler': page_handler,
        'product_head': product_head,
        'catalogue': catalogue,
        'gallery': gallery,
        'vsg': vsg,
        'lc1': lc1,
        'lc2': lc2,
        'lc3': lc3,
        'lc4': lc4,
        'is1': is1,
        'is2': is2,
    })


def product(request, product_name) :

    try : 
        product = Product.objects.get(product_name=product_name)
    except :
        product = None

    if product != None :

        gallery = Looper_Section.objects.filter(page_name='gallery')

        product_head = Product.objects.all()

        catalogue = Catalogue.objects.all()

        vsg = VSG.objects.all()

        sheets = Sheet.objects.filter(fk=product).order_by('-index')
        page = request.GET.get('page')
        paginator = Paginator(sheets, 12)
        last = paginator.num_pages 

        try : 
            sheet = paginator.page(page)
        except PageNotAnInteger :
            sheet = paginator.page(1)
        except EmptyPage :
            sheet = paginator.page(paginator.num_pages)

        return render(request, 'product.html', {
            'product_head': product_head,
            'catalogue': catalogue,
            'gallery': gallery,
            'vsg': vsg,
            'product': product,
            'sheet': sheet,
            'last': last,
        })
    
    else :

        return HttpResponse("Product not found !")


def product_tab(request, product_name, finish) :

    try : 
        product = Product.objects.get(product_name=product_name)
    except :
        product = None 

    if product != None :

        gallery = Looper_Section.objects.filter(page_name='gallery')

        product_head = Product.objects.all()

        catalogue = Catalogue.objects.all()

        vsg = VSG.objects.all()

        if finish != 'solid_colour':

            sheet = Sheet.objects.filter(main_finish=finish)

            return render(request, 'product.html', {
                'product_head': product_head,
                'catalogue': catalogue,
                'gallery': gallery,
                'vsg': vsg,
                'product': product,
                'sheet': sheet,
            })

        else :

            sheet = Sheet.objects.filter(main_finish=finish)

            return render(request, 'product-2.html', {
                'product_head': product_head,
                'catalogue': catalogue,
                'gallery': gallery,
                'vsg': vsg,
                'product': product,
                'sheet': sheet,
            })

    else :
        return HttpResponse("Product not found 2 !")


def gallery(request, pk) :

    try : 
        page_handler = Page_Handler.objects.get(page_name='gallery')
    except :
        return HttpResponse("Page Handler Error, About page not found !")

    gallery = Looper_Section.objects.filter(page_name='gallery')

    product_head = Product.objects.all()

    catalogue = Catalogue.objects.all()

    vsg = VSG.objects.all()
    
    try : 
        ls = Looper_Section.objects.get(pk=pk)
        lc = Looper_Component.objects.filter(fk=ls).order_by('index')
    except :
        lc = None

    return render(request, 'gallery.html', {
        'page_handler': page_handler,
        'product_head': product_head,
        'catalogue': catalogue,
        'gallery': gallery,
        'vsg': vsg,
        'lc': lc,
    })


def catalogue(request, cata_name) :

    if cata_name == 'pvc-laminate' :

        return render(request, 'catalogue_1.html')

    elif cata_name == 'charco-charm' :

        return render(request, 'catalogue_2.html')
        
    
def contact(request) : 

    contact_us = Contact_Us.objects.all()

    gallery = Looper_Section.objects.filter(page_name='gallery')

    product_head = Product.objects.all()

    catalogue = Catalogue.objects.all()

    vsg = VSG.objects.all()

    try : 
        ls = Looper_Section.objects.get(name='contact')
        lc = Looper_Component.objects.filter(fk=ls).order_by('index')
    except :
        lc = None

    return render(request, 'contact.html', {
        'contact_us': contact_us,
        'product_head': product_head,
        'catalogue': catalogue,
        'gallery': gallery,
        'vsg': vsg,
        'lc': lc,
    })


def policy_privacy(request) :

    try : 
        page_handler = Page_Handler.objects.get(page_name='privacy')
    except :
        return HttpResponse("Page Handler Error, About page not found !")

    gallery = Looper_Section.objects.filter(page_name='gallery')

    product_head = Product.objects.all()

    catalogue = Catalogue.objects.all()

    vsg = VSG.objects.all()

    return render(request, 'policy_privacy.html', {
        'page_handler': page_handler,
        'product_head': product_head,
        'catalogue': catalogue,
        'gallery': gallery,
        'vsg': vsg,
    })


def policy_terms(request) :

    try : 
        page_handler = Page_Handler.objects.get(page_name='terms')
    except :
        return HttpResponse("Page Handler Error, About page not found !")

    gallery = Looper_Section.objects.filter(page_name='gallery')

    product_head = Product.objects.all()

    catalogue = Catalogue.objects.all()

    vsg = VSG.objects.all()

    return render(request, 'policy_terms.html', {
        'page_handler': page_handler,
        'product_head': product_head,
        'catalogue': catalogue,
        'gallery': gallery,
        'vsg': vsg,
    })


def search(request) :

    search = request.GET.get('search', '')

    if search :

        try : 
            page_handler = Page_Handler.objects.get(page_name='search')
        except :
            return HttpResponse("Page Handler Error, About page not found !")

        gallery = Looper_Section.objects.filter(page_name='gallery')

        product_head = Product.objects.all()

        catalogue = Catalogue.objects.all()

        vsg = VSG.objects.all()

        a = Sheet.objects.filter(name__contains=search)
        b = Sheet.objects.filter(number__contains=search)

        sheets = list(chain(a,b))
        sheets = list(dict.fromkeys(sheets))

        paginator = Paginator(sheets, 12)
        page = request.GET.get('page')

        try:
            sheet = paginator.get_page(page)
        except PageNotAnInteger:
            sheet = paginator.page(1)
        except EmptyPage:
            sheet = paginator.page(paginator.num_pages)


        return render(request, 'search.html', {
            'page_handler': page_handler,
            'product_head': product_head,
            'catalogue': catalogue,
            'gallery': gallery,
            'sheet': sheet,
            'sheets': sheets,
            'search': search,
        })
    
    else :
        return HttpResponse("404")





