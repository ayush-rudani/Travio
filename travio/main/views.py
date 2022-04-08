
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .models import Package
from .models import Booking
from .models import Userdata
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request):
    return render(request, "register.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpswd = request.POST['cpswd']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('Login')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Login')

        # if len(username)>20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('Login')

        if password != cpswd:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Login')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('Login')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(
            request, "Your Account has been created succesfully!!")
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
        user = authenticate(username=username, password=password)

        print("Before login")
        print(username, password)

        if user is not None:
            print("yes")
            login(request, user)
            if username == "add":
                return redirect('adminpanel')
            messages.error(request, 'Sucessfully Logged in')
            return redirect('index')
        else:
            print("no")
            messages.error(request, 'Invalid Credentials')
            return redirect('Login')

    return redirect('register')


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def adminpanel(request):
    return render(request, "adminpage.html")


def addtour(request):
    return render(request, "addtour.html")


def addhotel(request):
    return render(request, "addhotel.html")


def viewtour(request):
    tour = Package.objects.all()
    return render(request, 'viewtour.html', {'tour': tour})


def viewuser(request):
    user = User.objects.all()
    return render(request, 'viewuser.html', {'user': user})


def viewhotel(request):
    hotels = Hotel.objects.all()
    return render(request, 'viewhotel.html', {'hotels': hotels})


def viewbooking(request):
    bookings = Booking.objects.all()
    return render(request, 'viewbooking.html', {'bookings': bookings})


def addt(request):
    if request.method == 'POST':
        tid = request.POST.get("tourId")
        ptitle = request.POST.get("ptitle")
        ttype = request.POST.get("type")
        # img1 = request.POST.get("image1")
        # img2 = request.POST.get("image2")
        img1 = request.FILES.get("image1")
        img2 = request.FILES.get("image2")
        tdes = request.POST.get("packageDesc")
        d = request.POST.get("duration")
        price = request.POST.get("disPrice")
        # ptitle = request.POST['packageTitle']
        # ttype = request.POST['type']
        # img1 = request.POST['image1']
        # img2 = request.POST['image2']
        # tdes = request.POST['packageDesc']
        # d = request.POST['duration']
        # price = request.POST['disPrice']

        tour = Package.objects.create(tourId=tid, packageTitle=ptitle, type=ttype,
                                      image1=img1, image2=img2, packageDesc=tdes, duration=d, price=price)
        tour.save()
    return redirect('adminpanel')


def addh(request):
    if request.method == 'POST':
        hotelId = request.POST.get("hotelId")
        hotelName = request.POST.get("hotelName")
        city = request.POST.get("city")
        hotelAddress = request.POST.get("hotelAddress")
        pincode = request.POST.get("pincode")
        hotelDesc = request.POST.get("hotelDesc")
        roomType = request.POST.get("roomType")
        price = request.POST.get("price")
        # image = request.POST.get("image")
        image = request.FILES.get("image")
        status = request.POST.get("status")

        hotel = Hotel.objects.create(hotelId=hotelId, hotelName=hotelName, city=city, hotelAddress=hotelAddress,
                                     pinCode=pincode, hotelDesc=hotelDesc, roomType=roomType, price=price, image=image, status=status)
        hotel.save()
    return redirect('adminpanel')


def hotel(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel.html', {'hotels': hotels})


def hDetails(request, name):
    hotel = Hotel.objects.all().filter(hotelId=name)
    return render(request, 'hoteldetails.html', {'hotel': hotel})


def booking(request, hname):
    print(hname)
    if Hotel.objects.filter(hotelName=hname).exists():
        book = Hotel.objects.all().filter(hotelName=hname)
        return render(request, 'booking.html', {'book': book})
    else:
        book = Package.objects.all().filter(packageTitle=hname)
        return render(request, 'booking.html', {'book': book})


def payment(request, hname):
    if Hotel.objects.filter(hotelName=hname).exists():
        hname = Hotel.objects.all().filter(hotelName=hname)
        bn = hname.hotelName
        bfair = hname.price
        type = 0
    elif Package.objects.filter(packageTitle=hname).exists():
        hname = Package.objects.all().filter(packageTitle=hname)
        bn = hname.packageTitle
        bfair = hname.bookingFair
        type = 1
    else:
        bfair = 0
    # hname = Hotel.objects.all().filter(hotelName = hname)
    # i = Counter().id
    user = request.user

    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        cnt = request.POST['cnt']
        people = request.POST['people']
        tdate = request.POST['tdate']
        #  Add dynamically userid here

        hbooking = Booking(uid=user.id, fname=fname, email=email, contact=cnt,
                           people=people, tdate=tdate, bookingName=hname, bookingFair=bfair)
        hbooking.save()
        print('Booking info added')
        messages.info(request, 'Booking info added')

        context = {}
        context['hname'] = hname
        context['user'] = user
        context['booking_details'] = hbooking
    return render(request, "receipt.html", context)


def receipt(request, hname):
    if Hotel.objects.filter(hotelName=hname).exists():
        hname = Hotel.objects.all().filter(hotelName=hname)
        return render(request, 'receipt.html')
    elif Package.objects.filter(packageTitle=hname).exists():
        hname = Package.objects.all().filter(packageTitle=hname)
        return render(request, 'receipt.html')
    # return render(request,"receipt.html",{'hname':hname})


def vacation(request):
    return render(request, "vacation.html")


def adventure(request):
    package = Package.objects.all()
    return render(request, 'adventure.html', {'package': package})
    # filter(type='Adventure')


def tDetails(request):
    return render(request, 'tourdetails.html')


def profile(request):
    user = request.user
    return render(request, "profilepage.html", {'user': user})


def tHistory(request):
    user = request.user
    history = Booking.objects.all().filter(uid=user.id)
    return render(request, "tourhistory.html", {'history': history})

# class Counter:
#     count = 0
#     id = 0

#     @classmethod
#     def incr(self):
#         self.count += 1
#         return self.count

#     def __init__(self):
#         self.id = self.incr()


def Logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Login')
