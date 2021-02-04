from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from User.models import Account ,Product ,Image
from django.contrib.auth.decorators import login_required
import re
import math
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.forms import formset_factory
from Xyzlo.settings import ALLOWED_HOSTS

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
        emailadd = request.POST.get('EmailId')
        password = request.POST.get('Password')
        cpassword = request.POST.get('CPassword')
        if(password != cpassword):
            messages.error(request, "password doesnot match.")
            return redirect("signup")
        if(bool(re.search(r'\d', name))):
            messages.error(request, "Name should not contain digits.")
            return redirect("signup")
        else:
            userlist=Account.objects.filter(email=emailadd)
            if(len(userlist) == 1):
                messages.error(request, "Xzylo Account with this email already exist.")
                return redirect("signup")
            else:
                user = Account.objects.create_user(name=name, email=emailadd, password=password, pnumber=pnumber,
                address=address, bdate=date)
                # for email verification it is set to false.It is set temporary set to true for login to work
                # before buying domain name.  
                user.is_active = False  
                user.save()
                current_site = "http://"+ALLOWED_HOSTS[0]
                # current_site = "http://XYZLOawsenv.eba-srdsknxu.ap-south-1.elasticbeanstalk.com"
                # print(current_site)
                message = render_to_string('acc_active_email.html', {
                    'user':user, 
                    # 'domain':current_site.domain,
                    'domain':current_site,
                    'uid':force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = 'Activate your Xyzlo account.'
                to_email = emailadd
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                messages.success(request,"Verfication mail has been send.Please confirm your email address to complete the registration",extra_tags="signupmsg")
                return redirect("login")
    
    else:
        messages.error(request, "Xzylo account not successfully created.")
        return HttpResponse('404 - Not found')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        messages.success(request, "Thank you for your email confirmation.Xzylo account successfully created.Now you can login your account")
        return redirect("login")
    else:
        return HttpResponse('Activation link is invalid!')

# @login_required
def home(request):
    if(str(request.user)=="AnonymousUser"):
        return redirect('login')
    else:
        return render(request, "home.html")
    # if request.user.is_authenticated:
    #     return redirect("signup")
    # else:

@login_required
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
        # print(loginemail,loginpassword)
        user = authenticate(email=loginemail, password=loginpassword)
        # login(request, user)
        # print(user)
        # return render(request, "home.html")
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

@login_required
def addpost(request):
    products = Product.objects.filter(pro_email=request.user.email)
    parameter = {'product':products}
    return render(request, "postadd.html", parameter)


def post(request):
    if request.method == 'POST':
        product_name = request.POST.get('Name')
        product_price = request.POST.get('Price')
        product_category = request.POST.get('Category')
        product_description = request.POST.get('description')
        product_location = request.POST.get('location')
        files=request.FILES.getlist('files')
        display_image=files[0]
        # # product_image = request.FILES[]
        # try:
        #     files=request.FILES.getlist('files')
        #     print(files[0])
        #     for i in range(1,len(files)):
        #         print(files[i])
        #     #     # a = Image(image=f)
        #     #     print(f)
        # except:
        #     print("Not found")

        current_user=request.user 

        pro_email = current_user.email
        productOnwer_name = current_user.name
        productOnwer_address = current_user.address
        # productOnwer_bdate = current_user.bdate
        productOnwer_pnumber = current_user.pnumber

        if(bool(re.search(r'\d', product_name))):
            messages.error(request, "Name should not contain digits.")
            return redirect("addpost")

        # # if(product_image==None):
        # #     messages.error(request, "Image field empty.")
        # #     return redirect("addpost")

        else:
            product = Product(pro_email=pro_email,productOnwer_name=productOnwer_name,
            productOnwer_address=productOnwer_address,
            productOnwer_pnumber=productOnwer_pnumber,product_name=product_name, product_price=product_price,
            product_category=product_category, product_description=product_description,
            product_location=product_location, product_image=display_image)
            product.save()
            for i in range(0,len(files)):
                product_img=Image(product=product,image=files[i])
                product_img.save()
                print(files[i])
            # try:
            #     print(product.pro_email)
            # except product.pro_email.DoesNotExist:
            #     print("////////////////////////////")
            messages.success(request, "Product uploaded successfully.")
            return redirect("home")
    
    return HttpResponse('postadded.')

@login_required
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
        products=Product.objects.filter(~Q(pro_email = request.user.email)).filter(product_category=choice)
        n= len(products)
        if(n>0):
            nSlides = n//4 + math.ceil((n/4) + (n//4))
            parameter = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product': products}
            return render(request, "buyrentchoices.html",parameter)
        else:
            messages.success(request, "Nothing to show.")
            nSlides = n//4 + math.ceil((n/4) + (n//4))
            parameter = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product': products}
            return render(request, "buyrentchoices.html",parameter)
    else:
        messages.error(request, "Choice not selected")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    return  HttpResponse('Choice page')


def userpost(request):
    products = Product.objects.filter(pro_email=request.user.email)
    parameter = {'product':products}
    return render(request, "userpost.html",parameter)


def deletepostmutiple(request):
    if request.method == 'POST':
        ans= request.POST.getlist('checkbox')
        if(len(ans)>0):
            while(len(ans) > 0):
                x=ans[0]
                ans.pop(0)
                Product.objects.filter(product_id=x).delete()
            # messages.success(request, "Product deleted successfully.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Product not selected")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse('Delete post')
    
def productDetails(request,product_id):
    products = Product.objects.filter(product_id=product_id)
    images= Image.objects.filter(product_id=product_id)
    parameter = {'product':products,'Images':images}
    return render(request, "productdetails.html",parameter)


def deletepost(request,product_id):
    Product.objects.filter(product_id=product_id).delete()
    products = Product.objects.filter(pro_email=request.user.email)
    parameter = {'product':products}
    messages.success(request, "Product deleted successfully.")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, "userpost.html",parameter)

def filterpost(request):
    if(request.method=='POST'):
        choice= request.POST.getlist('postchoice')
        category = request.POST.get('category')
        products = Product.objects.filter(~Q(pro_email = request.user.email))
        if(choice[0] == 'phtl'):
            products = products.filter(product_category=category).order_by('product_price').reverse()
            n= len(products)
            nSlides = n//4 + math.ceil((n/4) + (n//4))
            parameter = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product': products}
            return render(request, "buyrentchoices.html",parameter)
        elif(choice[0] == 'plth'):
            products = products.filter(product_category=category).order_by('product_price')
            n= len(products)
            nSlides = n//4 + math.ceil((n/4) + (n//4))
            parameter = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product': products}
            return render(request, "buyrentchoices.html",parameter)
        elif(choice[0] == 'lo'):
            # for time been the location is static ###################################################################
            products = products.filter(product_category=category).filter(product_location__icontains='Panvel')
            n= len(products)
            nSlides = n//4 + math.ceil((n/4) + (n//4))
            parameter = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product': products}
            return render(request, "buyrentchoices.html",parameter)
        else:
            messages.error(request, "Select the option")
            return  HttpResponse('Filtered Post') 
    return  HttpResponse('Filtered Post') 

def editpost(request,product_id):
    products = Product.objects.filter(product_id=product_id)
    parameter = {'product':products}
    return render(request, "editpost.html", parameter)

def edit_post(request, product_id):
    p = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        p.product_name = request.POST.get('Name')
        p.product_price = request.POST.get('Price')
        p.product_category = request.POST.get('Category')
        p.product_description = request.POST.get('description')
        p.product_location = request.POST.get('location')
        p.product_image = request.FILES['image']

        if(bool(re.search(r'\d', p.product_name))):
            messages.error(request, "Name should not contain digits.")
            return redirect("editpost", product_id=product_id)

        if(p.product_category.isalpha() == False):
            messages.error(request, "Category should only contain alphabets.")
            return redirect("editpost", product_id=product_id)

        else:
            p.save()
            messages.success(request, "Product edited successfully.")
            return redirect("productDetails", product_id=product_id)
    return HttpResponse('Post Edited')

