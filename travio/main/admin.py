from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import Package
from .models import Userdata

admin.site.register(Hotel)
admin.site.register(Package)
admin.site.register(Userdata)