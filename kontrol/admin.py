from django.contrib import admin
from kontrol.models import Station, Departure, Trip

# Register your models here.
admin.site.register(Station)
admin.site.register(Departure)
admin.site.register(Trip)

