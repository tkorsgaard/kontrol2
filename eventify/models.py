from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime


#from registration import models

class Event(models.Model):
    event_name = models.CharField(max_length=250)
    event_date = models.DateField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "<Event: %s on %s>" % (self.event_name, self.event_date)

    def get_absolute_url(self):
        return reverse('event-view', kwargs={'pk': self.id})




class Wish(models.Model):
    wish_name = models.CharField(max_length=250)
    wish_url = models.URLField()
    wish_price_low = models.IntegerField()
    wish_price_high = models.IntegerField()
    event = models.ForeignKey(Event)

    def __str__(self):
        return "<Wish: %s>" % (self.wish_name)


class Guest(models.Model):
    guset_name = models.CharField(max_length=250)
    guest_email = models.EmailField()
    wish = models.ForeignKey(Wish, null=True, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True)

    def __str__(self):
        return "<Guest: %s>" % (self.guset_name)

