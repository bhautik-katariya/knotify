from django.shortcuts import render,redirect
from .models import *
from Knotify.forms import *

# Create your views here.

def index(request):
    return render(request, 'invitee/calendar.html')

def date_event(request, date):
    return render(request,'invitee/event_details.html')

def edit_profile(request):
    eprofile = Invitee.objects.filter(username=request.session['username'])
    if request.method == 'POST':
        form = UserForm(request.POST,instance=eprofile)
        if form.is_valid():
            data = {
                'username':form.cleaned_data['username'],
                'f_name':form.cleaned_data['f_name'],
                'l_name':form.cleaned_data['l_name'],
                'email':form.cleaned_data['email'],
                'phone_no':form.cleaned_data['phone_no'],
                'password':form.cleaned_data['password'],
            }
            eprofile.update(**data)
            return redirect('invitee:index')
        else:
            form = UserForm(instance=eprofile)
        return render(request,'invitee/calendar.html')
