from django import forms
from django.core.exceptions import ValidationError
from Invitee.models import *
from Inviter.models import *
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    USER_ROLE = [
        ('invitee','Invitee'),
        ('inviter','Inviter'),
    ]
    user_role = forms.ChoiceField(choices=USER_ROLE,widget=forms.RadioSelect)
    username = forms.CharField(max_length=100)
    password =forms.CharField(max_length=100,widget=forms.PasswordInput())
    
class RegistrationForm(forms.Form):
    USER_ROLE = [
        ('invitee','Invitee'),
        ('inviter','Inviter'),
    ]
    user_role = forms.ChoiceField(choices=USER_ROLE,widget=forms.RadioSelect)
    username = forms.CharField(max_length=100)
    f_name = forms.CharField(max_length=100, label='First name') 
    l_name = forms.CharField(max_length=100, label='Last name')    
    email = forms.EmailField()  
    phone_no = forms.CharField(max_length=15) 
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user_role = self.cleaned_data['user_role']
        if user_role == 'invitee':
            if Invitee.objects.filter(username=username).exists():
                raise ValidationError("This username is already taken for Invitee.")
        elif user_role == 'inviter':
            if Inviter.objects.filter(username=username).exists():
                raise ValidationError("This username is already taken for Inviter.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user_role = self.cleaned_data['user_role']
        if user_role == 'invitee':
            if Invitee.objects.filter(email=email).exists():
                raise ValidationError("This email is already registered for Invitee.")
        elif user_role == 'inviter':
            if Inviter.objects.filter(email=email).exists():
                raise ValidationError("This email is already registered for Inviter.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords should be the same.")
        else:
            cleaned_data['password'] = make_password(password)
        return cleaned_data