from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enquiry

admin.site.register(Enquiry)
from django.contrib import admin

admin.site.site_header = "TravelYaari Admin"
admin.site.site_title = "TravelYaari Admin Portal"
admin.site.index_title = "Welcome to TravelYaari Administration"
