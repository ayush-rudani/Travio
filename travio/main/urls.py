from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('register',views.register,name="register"),
    path('contact',views.contact,name="contact"),
    path('hotel',views.hotel,name="hotel"),
    path('hDetails',views.hDetails,name="hDetails")
]
