
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .models import Package
from .models import Booking
from .models import Userdata
from django.contrib.auth import authenticate, login, logout
# import itertools

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

def hDetails(request,name):
    hotel = Hotel.objects.all().filter(hotelId = name)
    return render(request,'hoteldetails.html',{'hotel':hotel})

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

class Counter:
    count = 0
    id = 0

    @classmethod
    def incr(self):
        self.count += 1
        return self.count

    def __init__(self):
        self.id = self.incr()

def payment(request,hname):
    hname = Hotel.objects.all().filter(hotelName = hname)
    # i = itertools.count()
    i = Counter().id
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
    
        hbooking = Booking(i,1,fname,email,cnt,people,tdate,name,price)
        hbooking.save()
        print('Booking info added')
        messages.info(request,'Booking info added')
    return render(request,"payment.html",{'hname':hname})

def receipt(request,hname):
    hname = Hotel.objects.all().filter(hotelName = hname)
    return render(request,"receipt.html",{'hname':hname})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpswd = request.POST['cpswd']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Login')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Login')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('Login')
        
        if password != cpswd:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Login')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('Login')
        
        myuser = User.objects.create_user(username,email,password)
        # myuser.is_active = False
        # myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('Login')

    #     if password==cpswd:
    #         if User.objects.filter(username=username).exists():
    #             messages.error(request,'Username already taken')
    #         elif User.objects.filter(email=email).exists(): 
    #             messages.error(request,'Email already taken')
    #         else :
    #             user = User.objects.create(username=username,email=email,password=password)
    #             user.save()
    #             messages.error(request,'Registration successfull!!')
    #     else :
    #         messages.error(request,'Both password must be same')

    #     return redirect('signup')
    # else :
    #     return render(request,'register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)

        print("Before login")
        print(username,password)

        if user is not None:
            print("yes")
            login(request,user)
            messages.error(request, 'Sucessfully Logged in')
            return redirect('index')
        else:
            print("no")
            messages.error(request,'Invalid Credentials')
            return redirect('Login')

    return redirect('register')
    
def Logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Login')
        

