from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from User.models import Account ,Product
from django.contrib.auth.decorators import login_required
import re
import math

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


def addpost(request):
    return render(request, "postadd.html")

def post(request):
    if request.method == 'POST':
        product_name = request.POST.get('Name')
        product_price = request.POST.get('Price')
        product_category = request.POST.get('Category')
        product_description = request.POST.get('description')
        product_location = request.POST.get('location')
        product_image = request.POST.get('image')

        # print(product_name,product_price,product_category,product_description,
        # product_location,product_image)

        if(bool(re.search(r'\d', product_name))):
            messages.error(request, "Name should not contain digits.")
            return redirect("addpost")

        # # if(product_image==None):
        # #     messages.error(request, "Image field empty.")
        # #     return redirect("addpost")




        else:
            product = Product(product_name=product_name, product_price=product_price,
            product_category=product_category, product_description=product_description,
            product_location=product_location, product_image=product_image)
            # try:
            #     print(product.pro_email)
            # except product.pro_email.DoesNotExist:
            #     print("////////////////////////////")
            product.save()
            messages.success(request, "Product uploaded successfully.")
            return redirect("home")
    
    return HttpResponse('postadded.')

def buyrent(request):
    products = Product.objects.all()
    choices=[]
    for i in products:
        if(i.product_category not in choices):
            choices.append(i.product_category)
        else:
            continue
    parameter = {'choices':choices}
    return render(request, "buyrent.html",parameter)


def buyrentchoice(request):
    if request.method == 'POST':
        choice= request.POST.get('Choice')
        products = Product.objects.filter(product_category=choice)
        n= len(products)
        nSlides = n//4 + math.ceil((n/4) + (n//4))
        parameter = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product': products}
        return render(request, "buyrentchoices.html",parameter)
    else:
        messages.error(request, "Choice not selected")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


    
