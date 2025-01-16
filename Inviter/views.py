from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Knotify.forms import *

# Create your views here.

def dashboard(request):
    username=request.session['username']
    inviter = Inviter.objects.get(username=username)
    events = EventDetails.objects.filter(inviter=inviter)
    return render(request,'inviter/dashboard.html',{'events':events, 'username':username})

def add_event(request): 
    if request.method == 'POST':
        form = EventForm(request.POST)  
        if form.is_valid():
            event = form.save(commit=False)
            username = request.session['username']
            inviter = Inviter.objects.get(username=username)
            event.inviter = inviter
            event.save()
            return redirect('inviter:dashboard')
    else:
        form = EventForm()
    return render(request,'inviter/event_form.html',{'form':form})

def event_update(request,event_id):  
    edetails = EventDetails.objects.get(pk=event_id)
    if request.method == 'POST':                                            
        form = EventForm(request.POST, instance=edetails)
        if form.is_valid():
            if request.session['username'] == 'admin':
                form.inviter = edetails.inviter
            form.save()
            return redirect('inviter:dashboard')
    else:
        form = EventForm(instance=edetails)
    return render(request,'inviter/event_update.html', {'form':form})

