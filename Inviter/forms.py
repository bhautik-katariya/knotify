from .models import *
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        exclude = ['username']