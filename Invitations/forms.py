from django import forms
from .models import *

class inviter_form(forms.ModelForm):
    class Meta:
        model = Inviter
        fields = ['phone_no','password']
        
class invites_form(forms.ModelForm):
    class Meta:
        model = Invites
        fields = ['guest_no','password']