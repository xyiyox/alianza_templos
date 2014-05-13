from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Proyecto

admin.site.register(Proyecto, LeafletGeoAdmin)
