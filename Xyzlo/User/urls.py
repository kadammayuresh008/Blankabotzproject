from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginpage, name="login"),
    path('signup/', views.signuppage, name="signup"),
    path('signup/signIn/', views.signIn, name="SignIn"),
    path('login/handlelogin/', views.handlelogin, name="handlelogin"),
    path('about/', views.about, name="about"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('addpost/', views.addpost, name="addpost"),
    path('buyrent/', views.buyrent, name="buyrent"),
    path('post', views.post , name="post"),
    path('buyrent/buyrentchoice/', views.buyrentchoice, name="buyrentchoice"),
    path('userpost/',views.userpost ,name="userpost"),
    path('deletepost/deletepostmutiple/',views.deletepostmutiple,name="delete_userpost"),
    path('userpost/deletepostmutiple/',views.deletepostmutiple ,name="deletepostmutiple"),
    path('productdetails/<product_id>',views.productDetails, name="productDetails"),
    path('deletepost/<product_id>',views.deletepost, name="deletepost"),
    path('buyrent/buyrentchoice/filterpost', views.filterpost ,name="filterpost"),
    path('editpost/<product_id>',views.editpost, name="editpost"),
    path('edit_post/<product_id>', views.edit_post , name="edit_post"),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate')
]