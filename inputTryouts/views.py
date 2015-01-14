from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse
from eventify.models import Event, Wish, Guest
from inputTryouts.models import Person, DateTryout
# Create your views here.

from inputTryouts.forms import PersonForm

class ListPersonView(ListView):
    model = Person
    #code
    #object_list = Event.objects.filter(user = self.request.user)
    template_name = 'person_list.html'

class CreatePersonView(CreateView):
    model = Event
    template_name = 'create_person.html'
    #form_class = ContactForm
    form_class = PersonForm

    def get_sucess_url(self):
        return reverse('person-list')