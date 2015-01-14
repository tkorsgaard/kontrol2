import floppyforms.__future__ as forms

from kontrol.models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        #exclude = ('user',)
        fields = ('trip_date', 'departure', 'tickets_checked','checked_after', 'bike')
