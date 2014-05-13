from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *

admin.site.register(Proyecto, LeafletGeoAdmin)
admin.site.register(Edificacion, LeafletGeoAdmin)
admin.site.register(Comunidad)
admin.site.register(Fuentes_Financieras)
admin.site.register(Condiciones)
admin.site.register(Edificacion_Condiciones)
admin.site.register(Preguntas)

