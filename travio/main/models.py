from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Hotel(models.Model):
    hotelId = models.IntegerField(primary_key=True)
    hotelName = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    hotelAddress = models.TextField()
    pinCode = models.IntegerField()
    hotelDesc = models.TextField()
    roomType = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=50,default='hotel1.webp')

    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    STATUS = [
       (AVAILABLE,('Available')),
       (UNAVAILABLE,('Unavailable')),
    ]
   # […]
    status = models.CharField(
       max_length=32,
       choices=STATUS,
       default=AVAILABLE,
   )

class Package(models.Model):
    tourId = models.IntegerField(primary_key=True)
    packageTitle = models.CharField(max_length=100)

    ADVENTURE = 'adventure'
    WILDLIFE = 'wildlife'
    PILGRIMAGE = 'pilgrimage'
    FAMILY = 'family'
    HONEYMOON = 'honeymoon'
    TYPE = [
       (ADVENTURE,('Adventure')),
       (WILDLIFE,('Wildlife')),
       (PILGRIMAGE,('Pilgrimage')),
       (FAMILY,('Family')),
       (HONEYMOON,('Honeymoon')),
    ]
   # […]
    type = models.CharField(
       max_length=32,
       choices=TYPE,
       default=ADVENTURE,
   )

    image1 = models.CharField(max_length=50,default='tour.jpg')
    image2 = models.CharField(max_length=50,default='tour.jpg')
    packageDesc = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.IntegerField()
    disPrice = models.IntegerField()
    discount = models.BooleanField()

class Userdata(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.CharField(max_length=50,default='tour.jpg')
    address = models.TextField(null=True)
    dob = models.DateField(null=True)
    contact = models.IntegerField(null=True)
    




    
