from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from Knotify.forms import *

# Create your views here.

def index(request):
    return HttpResponse('hello..............')

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
            return redirect('dashboard')
        else:
            form = UserForm(instance=eprofile)
        return render(request,'invitee/dashboard.html')
    
def inviter_events(request):
    event_details = EventDetails.objects.all()
    return render(request,{'event_details':event_details})