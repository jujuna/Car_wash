from django.contrib import admin

# Register your models here.
from .models import Location,WasherCompany,HireCompany

admin.site.register(WasherCompany)

admin.site.register(Location)
admin.site.register(HireCompany)