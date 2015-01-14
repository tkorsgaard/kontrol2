import datetime

import floppyforms.__future__ as forms
#from django import forms
#from floppyforms import forms
#from django.core.exceptions import ValidationError
#from django.forms.models import inlineformset_factory
##from django.forms.widgets import DateInput
from eventify.models import Event

#EventFormSet = inlineformset_factory(Event)

class EventForm(forms.ModelForm):

    #confirm_email = forms.EmailField(
    #    label='Confirm email',
    #    required=True,
    #)

    #event_date_dtp = forms.DateTimeField(
    #    label='Choose event date:',
    #    input_formats=['%m/%d/%Y'],
    #
    #
    #)

    class Meta:
        model = Event
        #exclude = ('user',)
        fields = ('event_name', 'event_date')
        #event_name = forms.CharField(required = False)
        #details = forms.CharField(widget = forms.Textarea())
        #event_date = forms.CharField(min_length = 10, widget = DateInput(format="%d-%m-%Y"))


