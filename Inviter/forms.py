from django import forms
from .models import *
from Invitee.models import *

class EventForm(forms.ModelForm):
    # invitees = forms.ModelMultipleChoiceField(
    #     queryset=Invitee.objects.all(),  # Fetch all invitees from the database
    #     widget=forms.CheckboxSelectMultiple,  # Render as checkboxes
    #     label="Select Invitees"
    # )
    class Meta:
        model = EventDetails
        exclude = ['inviter']
        widgets = {
            'e_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',  # HTML5 input for datetime-local
                    'class': 'form-control',  # Bootstrap class for styling (optional)
                }
            ),
            'invitee': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'invitee': 'Select Invitees',  # Custom label for invitee field
        }