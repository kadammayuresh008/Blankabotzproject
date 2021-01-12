# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User 
# from django.contrib import messages

# def signup(request):
#     return render(request, "signup.html")

# def login(request):
#     return render(request, "login.html")

# def signIn(request):
#     if request.method == 'POST':
#         name = request.POST.get('Name')
#         address = request.POST.get('Address')
#         date = request.POST.get('Date')
#         pnumber = request.POST.get('Pnumber')
#         email = request.POST.get('EmailId')
#         password = request.POST.get('Password')
#         cpassword = request.POST.get('CPassword')

#         # print(name, address, date, pnumber, email, password, cpassword)

#         user = User.objects.create_user(username=name, email=email, password=password)
#         user.address = address
#         user.date = date
#         user.pnumber = pnumber
#         user.save()
#         messages.success(request, "Xzylo account successfully created.")
#         return redirect("login")
    
#     else:
#         return HttpResponse('404 - Not found')




