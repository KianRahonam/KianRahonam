from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.loginPage, name="loginPage"),
    path("mainPage",views.mainPage, name="mainPage"),
    path('loading',views.loadingPage, name='loadingPage'),
    path("signup",views.signup, name='signup'),
    path("createUser", views.createUser, name='createUser'),
    path("loginUser", views.loginUser, name='loginUser'),
    path("mainView", views.mainview, name='mainView'),
    path("logoutUser", views.logoutUser, name='logoutUser'),
    path("userManagement", views.userManagement, name='userManagement'),
    path("bookingPage", views.bookingPage, name='bookingPage'),
    path("createBooking", views.createBooking, name='createBooking'),
    path('viewBooking', views.viewBooking,name='viewBooking'),
    path('viewDetials', views.viewDetials,name='viewDetials'),
    path('bookingReport', views.bookingReport, name='bookingReport'),
    path('updateBooking', views.bookingUpdatePage, name='updateBooking'),
    path('updareRecord', views.lrData, name='updateBooking'),
    path('newBranch', views.newBranch, name='newBranch'),
    path('createBranch', views.createBranch, name='createBranch'),
    path('lrDataUpdate',views.lrDataUpdate, name="lrDataUpdate"),
    path('loadingPage',views.loadingPage, name='loadingPage'),
    path('lorryhirePage',views.lorryhirePage, name='lorryhirePage'),
    path('lorryHire',views.lorryHire, name='lorryHire'),
    path('approve/<str:id>', views.approve, name='approve'),
    path('reject/<str:id>', views.reject, name='reject'),
    path('clearall',views.clearall, name='clearall'),
    path('track',views.track, name='track'),
    path('load_consignment', views.load_consignment, name='load_consignment'),
    path('uploadPod', views.uploadPod, name='uploadPod')
]