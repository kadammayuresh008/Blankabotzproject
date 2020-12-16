from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name="login"),
    path('signup/', views.signuppage, name="signup"),
    path('signup/signIn/', views.signIn, name="SignIn"),
    path('login/', views.handlelogin, name="handlelogin"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('addpost/', views.addpost, name="addpost"),
    path('buyrent/', views.buyrent, name="buyrent"),
    path('post', views.post , name="post"),
    path('buyrent/buyrentchoice/', views.buyrentchoice, name="buyrentchoice"),
    path('userpost/',views.userpost ,name="userpost"),
    path('userpost/deletepost/',views.deletepost ,name="deletepost"),
    path('productdetails/<product_id>',views.productDetails, name="productDetails"),
    path('deletepost/<product_id>',views.deletepost, name="deletepost"),
]