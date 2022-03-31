from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.register, name="register"),
    path('index',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('hotel',views.hotel,name="hotel"),
    path('hDetails',views.hDetails,name="hDetails"),
    path('vacation',views.vacation,name="vacation"),
    path('adventure',views.adventure,name="adventure"),
    path('tDetails',views.tDetails,name="tDetails"),
    path('profile',views.profile,name="profile"),
    path('tHistory',views.tHistory,name="tHistory"),
    path('payment',views.payment,name="payment"),
    path('receipt',views.receipt,name="receipt"),
]
