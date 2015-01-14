from django.contrib import admin
from eventify.models import Event, Wish, Guest

# Register your models here.

admin.site.register(Event)
admin.site.register(Wish)
admin.site.register(Guest)