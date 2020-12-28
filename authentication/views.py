from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def myregister(request) :

    if request.method == "POST" :

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        

        if pass1 != pass2 :
            msg = "Holy guacamole! You must have screwed up something, give it a one more try"
            return render(request, 'back/register.html', {
                'msg': msg,
            })

        if len(pass1) < 6 :
            msg = "Password length error, password at least needs to be 6 character long. \nFun Fact : Average human name contains 6 characters, you can always try it if you can not come up with a more secure password. On my count, One...Two...WAIT WAIT WAIT, Lemme double check no one's watching. Yeah you are good to go, ...Three... NOW NOW NOW !"
            return render(request, 'back/register.html', {
                'msg': msg,
            })

        # success
        if len(User.objects.filter(username=email)) == 0 and len(User.objects.filter(email=email)) == 0:
            user = User.objects.create_user(username=email, email=email, password=pass1, first_name=fname, last_name=lname)

            msg = "Voilà, Now you are only one step away. Go ahead and sign in ! " 

            return render(request, 'back/login.html', {
                'msg': msg,
            })
            
        else : 
            msg = "Voila, you are already associated with us. Look at you, we know you love as. Anyways, as you are already registered just go ahead and Sign yourself in. If you are lost and can not remember your password then try straining your brain a little more, im sure you'll remember it. If you still can't then dont worry we have got you, Click on Forgot Password and get yourself a brand new password !"
            return render(request, 'back/register.html', {
                'msg': msg,
            })


    return render(request, 'back/register.html')


def mylogin(request) :

    if request.method == 'POST' :

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(username=email, password=password)

        if user != None :
            
            login(request, user)
            return redirect('panel')

        else : 

            failure = "failure"

            return render(request, 'login.html', {
                'failure': failure,
            })


    return render(request, 'login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')
