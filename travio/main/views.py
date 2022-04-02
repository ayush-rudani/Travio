
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .models import Package
from .models import Userdata
from .models import Booking
# from .models import Userc

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

@login_required(login_url='/login')
def hDetails(request,name):
    hotel = Hotel.objects.all().filter(hotelId = name)
    return render(request,'hoteldetails.html',{'hotel':hotel})

@login_required(login_url='/login')
def booking(request,hname):
    book = Hotel.objects.all().filter(hotelName = hname)
    return render(request,'booking.html',{'book':book})

def vacation(request):
    return render(request,"vacation.html")

def adventure(request):
    package = Package.objects.all()
    return render(request,'adventure.html',{'package':package})
    # filter(type='Adventure')

def tDetails(request):
    return render(request,'tourdetails.html')

def profile(request):
    return render(request,"profilepage.html")

def tHistory(request):
    return render(request,"tourhistory.html")

@login_required(login_url='/login')
def payment(request,hname):
    hname = Hotel.objects.all().filter(hotelName = hname)

    for hb in hname :
        name = hb.hotelName
        price = hb.price

    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        cnt = request.POST['cnt']
        people = request.POST['people']
        tdate = request.POST['tdate']
        #  Add dynamically userid here
        hbooking = Booking(1,1,fname,email,cnt,people,tdate,name,price)
        hbooking.save()
        print('Booking info added')
        messages.info(request,'Booking info added')

    return render(request,"payment.html")

def receipt(request):
    return render(request,"receipt.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpswd = request.POST['cpswd']

        if password==cpswd:
            if Userdata.objects.filter(username=username).exists():
                print('Username already taken')
                messages.info(request,'Username already taken')
            elif Userdata.objects.filter(email=email).exists(): 
                print('Email already taken')
                messages.info(request,'Email already taken')
            else :
                user = Userdata.objects.create(username=username,email=email,password=password)
                user.save()
                print('user created')
                messages.info(request,'Registration successfull!!')
        else :
            print('PASSWORD NOT MATCHING')
            messages.info(request,'Both password must be same')

        return redirect('/')
    else :
        return render(request,'hotel.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('signup')
    else:
        return render(request,"register.html")

        

