from django.db import models

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
