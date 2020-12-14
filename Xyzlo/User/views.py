from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from User.models import Account
from django.contrib.auth.decorators import login_required
import re

def signuppage(request):
    return render(request, "signup.html")

def loginpage(request):
    return render(request, "login.html")

# signin function 
def signIn(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        address = request.POST.get('Address')
        date = request.POST.get('Date')
        pnumber = request.POST.get('Pnumber')
        email = request.POST.get('EmailId')
        password = request.POST.get('Password')
        cpassword = request.POST.get('CPassword')
        if(password != cpassword):
            messages.error(request, "password doesnot match.")
            return redirect("signup")
        if(bool(re.search(r'\d', name))):
            messages.error(request, "Name should not contain digits.")
            return redirect("signup")
        else:
            user = Account.objects.create_user(name=name, email=email, password=password, pnumber=pnumber,
            address=address, bdate=date)
            user.save()

            messages.success(request, "Xzylo account successfully created.")
            return redirect("login")
    
    else:
        messages.error(request, "Xzylo account not successfully created.")
        return HttpResponse('404 - Not found')


@login_required
def home(request):
    # if request.user.is_authenticated:
    #     return redirect("signup")
    # else:
    return render(request, "home.html")

def about(request):
    # if request.user.is_authenticated:
    #     return redirect("signup")
    # else:
    return render(request, "about.html")

# login function 
def handlelogin(request):
    if request.method == 'POST':
        loginemail = request.POST.get('Email')
        loginpassword = request.POST.get('password')
        user = authenticate(email=loginemail, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return render(request, "home.html")
        else:
            messages.error(request, "Invalid credentials.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse('handlelogin')

# logout function 
def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return render(request, "logout.html")



    
