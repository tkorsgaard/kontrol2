from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()

from eventify.models import Guest, Wish, Event
from inputTryouts.models import Person, DateTryout
from kontrol.models import Trip

import eventify.views
import inputTryouts.views
import kontrol.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WishAdmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #URL
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.default.urls')),

    #url(r'^$', eventify.views.ListEventView.as_view(),name='event-list'),

    #url(r'^details/(?P<pk>\d+)/$', eventify.views.DetailEventView.as_view(),name='event-view'),

    #url(r'^event/new$', eventify.views.CreateEventView.as_view(model=Event, success_url=reverse_lazy('event-list')),name='event-new'), #model=Contact, success_url=reverse('contacts-list')

    # for testing
    #url(r'^persons/new$', inputTryouts.views.CreatePersonView.as_view(model=Event, success_url=reverse_lazy('person-list')),name='person-new'), #model=Contact, success_url=reverse('contacts-list')

    #url(r'^persons/$', inputTryouts.views.ListPersonView.as_view(),name='person-list'),

    url(r'^trips/$', kontrol.views.ListTripsView.as_view(),name='trip-list'),

    url(r'^trips/new$', kontrol.views.CreateTripView.as_view(model=Trip, success_url=reverse_lazy('trip-list')),name='trip-new'), #model=Contact, success_url=reverse('contacts-list')

)
