from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotel
from .models import Package
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

def vacation(request):
    return render(request,"vacation.html")

def adventure(request):
    package = Package.objects.all()
    return render(request,'adventure.html',{'package':package})
    # filter(type='Adventure')

def tDetails(request):
    return render(request,"tourdetails.html")