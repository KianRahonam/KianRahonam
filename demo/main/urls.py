from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage, name='main'),
    path('loginUser',views.loginUser, name='login'),
    path('adduser',views.adduserPage, name="adduserPage"),
    path('createUser',views.adduser,name='createuser')
]
