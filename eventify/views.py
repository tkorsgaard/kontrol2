from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse
from eventify.models import Event, Wish, Guest

from eventify.forms import EventForm #, EventFormSet

class ListEventView(ListView):
    model = Event
    #code
    #object_list = Event.objects.filter(user = self.request.user)
    template_name = 'event_list.html'

    def get_queryset(self):
        #self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Event.objects.filter(user=self.request.user)

class DetailEventView(DetailView):
    model = Event
    template_name = 'event.html'


class CreateEventView(CreateView):
    model = Event
    template_name = 'create_event.html'
    #form_class = ContactForm
    form_class = EventForm

    def get_sucess_url(self):
        return reverse('event-list')


    #def get_context_data(self, **kwargs):
    #    context = super(CreateContactView, self).get_context_data(**kwargs)
    #    context['action'] = reverse('contacts-new')
    #
    #    return context




