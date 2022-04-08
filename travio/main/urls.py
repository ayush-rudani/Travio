from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.register, name="register"),
    path('signup', views.signup, name="signup"),
    path('Login', views.Login, name="Login"),
    path('index', views.index, name="index"),
    path('hotel', views.hotel, name="hotel"),
    path('hDetails/<str:name>', views.hDetails, name="hDetails"),
    path('hDetails/booking/<str:hname>', views.booking, name="booking"),
    path('hDetails/booking/payment/<str:hname>', views.payment, name="payment"),
    path('hDetails/booking/payment/receipt/<str:hname>',
         views.receipt, name="receipt"),
    path('vacation', views.vacation, name="vacation"),
    path('adventure', views.adventure, name="adventure"),
    path('tDetails', views.tDetails, name="tDetails"),
    path('profile', views.profile, name="profile"),
    path('tHistory', views.tHistory, name="tHistory"),
    path('payment', views.payment, name="payment"),
    path('receipt', views.receipt, name="receipt"),
    path('contact', views.contact, name="contact"),
    path('Logout', views.Logout, name="Logout"),

    path('adminpanel', views.adminpanel, name="adminpanel"),
    path('addtour', views.addtour, name="addtour"),
    path('addt', views.addt, name="addt"),
    path('viewtour', views.viewtour, name="viewtour"),
    path('viewuser', views.viewuser, name="viewuser"),
    path('addhotel', views.addhotel, name="addhoetl"),
    path('viewhotel', views.viewhotel, name="viewhotel"),
    path('viewbooking', views.viewbooking, name="viewbooking"),
    path('addh', views.addh, name="addh"),
]
