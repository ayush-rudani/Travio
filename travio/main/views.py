from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotel

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request,"register.html")

def contact(request):
    return render(request,"contact.html")

def hotel(request):
    hotels = Hotel.objects.all()
    return render(request,'hotel.html',{'hotels':hotels})

def hDetails(request):
    return render(request,"hoteldetails.html")
