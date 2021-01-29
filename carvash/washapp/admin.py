from django.contrib import admin

# Register your models here.
from .models import Washer,Car,Order
admin.site.register([Washer,Car,Order])