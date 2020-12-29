import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from contact.models import Contact_Us, Lead
from product.models import Product
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from django.contrib import messages



def contact_back(request):


    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')



    contact = Contact_Us.objects.all()


    lead = Lead.objects.all().order_by('-pk')


    return render(request, 'contact_back.html', {
        'contact': contact,
        'lead': lead,
    })



def contact_add(request):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')



    if request.method == 'POST':

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        url = request.POST.get('url', '')

        contact = Contact_Us(
            meta_title = meta_title,
            meta_description = meta_description,
            email = email,
            phone = phone,
            address = address,
            url = url,
        )

        contact.save()

        msg = "Contact info has been updated !"
        messages.success(request, msg)

        return redirect('contact_back')

    else :
        return HttpResponse('Error happened while sending data via POST method !')



def contact_edit(request, contact_pk):

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == 'POST':

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        url = request.POST.get('url', '')

        try:
            contact = Contact_Us.objects.get(pk=contact_pk)
        except Contact_Us.DoesNotExist:
            contact = None    

        if contact != None :

            contact.meta_title = meta_title
            contact.meta_description = meta_description
            contact.email = email
            contact.phone = phone
            contact.address = address
            contact.url = url

            contact.save()

            msg = "Contact info has been updated !"
            messages.success(request, msg)

            return redirect('contact_back')

        else :
            return HttpResponse("Contact object not found while tried editing ! ")



    return render(request, 'contact_back.html')



def lead(request) :

    name_ = request.POST.get('name', '')
    email_ = request.POST.get('email', '')
    message_ = request.POST.get('message', '')
    now =  datetime.datetime.now()

    time_ = str(now.day) + ' / ' + str(now.month) + ' / ' + str(now.year) + ' AT ' + str(now.hour) + " : " + str(now.minute) 


    message ="Inquiry Generated From Website 'rangdecor.in' <br><br>" + "Name : " + name_ + "<br><br>Email : " + email_ + "<br><br>Inquiry Detail : " + message_ +  "<br><br><br><br><br><br>Thank You, Team KrioskCreata."

    email = EmailMessage("Inquiry from website [rangdecor.in]", message, settings.EMAIL_HOST_USER, ['info@rangdecor.in'])

    email.content_subtype = 'html'

    # files = request.FILES.get('image', None)
    # email.attach(files.name, files.read(), files.content_type)

    email.send()

    lead = Lead(
        name = name_,
        email = email_,
        time = time_,
        message = message_,
        revert = False
        
    )

    lead.save()


    msg = " "
    messages.success(request, msg)


    return redirect('contact')



def lead_view(request, lead_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    try:
        lead = Lead.objects.get(pk=lead_pk)
    except Lead.DoesNotExist:
        lead = None    

    if lead != None :

        return render(request, 'lead_view.html', {
            'lead': lead,
        })



def lead_revert(request, lead_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')

    if request.method == 'POST' :

        try:
            lead = Lead.objects.get(pk=lead_pk)
        except Lead.DoesNotExist:
            lead = None    

        if lead != None :

            title_ = request.POST.get('title', '')
            message_ = request.POST.get('message', '')
            mail = lead.email
            
            
            email = EmailMessage(title_, message_, settings.EMAIL_HOST_USER, [mail])

            email.content_subtype = 'html'

            email.send()

            lead.revert = True
            lead.save()

            msg = "Reply email has been genereted and automation system will soon delever it ! For more queries check your outbox/sent folder !"
            messages.success(request, msg)

            return redirect('contact_back')

        else : 
            return HttpResponse("Lead object not found while reverting !")


    try:
        lead = Lead.objects.get(pk=lead_pk)
    except Lead.DoesNotExist:
        lead = None    

    if lead != None :

        return render(request, 'lead_revert.html', {
            'lead': lead,
        })



def lead_delete(request, lead_pk) :

    # Controlling User Access to Control Panel
    if not request.user.is_authenticated :
        return redirect('mylogin')



    try:
        lead = Lead.objects.get(pk=lead_pk)
    except Lead.DoesNotExist:
        lead = None    

    if lead != None :

        lead.delete()

        msg = "Lead has been deleted !"
        messages.success(request, msg)

        return redirect('contact_back')
    
    else :
        return HttpResponse("Could not delete lead, refresh the page and try again !")




