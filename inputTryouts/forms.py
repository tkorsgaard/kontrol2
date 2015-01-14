import floppyforms.__future__ as forms
from inputTryouts import models

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ('full_name', 'email', 'has_work', 'date_of_birth')
        #widgets = {
        #    'full_name': forms.TextInput,
        #    'email': forms.EmailInput,
        #    'has_work': forms.BooleanField,
        #}