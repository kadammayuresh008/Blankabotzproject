from django.urls import path
from . import views

urlpatterns = [
    path('', views.signuppage, name="signup"),
    path('loginpage/', views.loginpage, name="login"),
    path('signIn/', views.signIn, name="SignIn"),
    path('loginpage/login/', views.handlelogin, name="handlelogin"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('addpost/', views.addpost, name="addpost"),
    path('buyrent/', views.buyrent, name="buyrent"),
    path('post', views.post , name="post"),
    path('buyrent/buyrentchoice/', views.buyrentchoice, name="buyrentchoice"),
    path('userpost/',views.userpost ,name="userpost"),
    path('userpost/deletepost/',views.deletepost ,name="deletepost"),
    path('productdetails/',views.productDetails, name="productDetails"),
]