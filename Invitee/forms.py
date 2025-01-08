from django import forms
from .models import *
from django.contrib.auth.hashers import make_password

class InviteeRegistration(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    
    class Meta:
        model = Invitee
        fields = '__all__'
        widgets = {
            'password':forms.PasswordInput(),
        }
        
    def save(self,commit=True):
        password = self.cleaned_data['password']
        self.cleaned_data['password']=make_password(password)
        return super().save(commit=commit)
    
    
    