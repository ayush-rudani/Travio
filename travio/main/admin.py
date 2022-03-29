from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import Package

admin.site.register(Hotel)
admin.site.register(Package)