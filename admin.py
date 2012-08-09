#from django.contrib.gis import admin
from django.contrib import admin

from models import *

class Admin(admin.OSMGeoAdmin):
    pass

#admin.site.register(, Admin)

