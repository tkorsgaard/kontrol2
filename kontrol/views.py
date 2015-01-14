from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse
from kontrol.models import Trip

from kontrol.forms import TripForm

class ListTripsView(ListView):
    model = Trip
    #code
    #object_list = Event.objects.filter(user = self.request.user)
    template_name = 'trip_list.html'

class CreateTripView(CreateView):
    model = Trip
    template_name = 'create_trip.html'
    #form_class = ContactForm
    form_class = TripForm

    def get_sucess_url(self):
        return reverse('trip-list')
