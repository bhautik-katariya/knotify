from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Knotify.forms import *

# Create your views here.

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)  
        if form.is_valid():
            event = form.save(commit=False)
            username = request.session['username']
            inviter = Inviter.objects.filter(username=username)
            event.inviter = inviter
            event.save()
            return redirect('inviter:dashboard')
    else:
        form = EventForm()
    return render(request,'inviter/event_form.html',{'form':form})

def dashboard(request):
    username=request.session['username']
    inviter = Inviter.objects.filter(username=username)
    events = EventDetails.objects.filter(inviter=inviter)
    return render(request,'inviter/dashboard.html',{'events':events})

def event_update(request,id): 
    edetails = EventDetails.objects.get(id = id)
    if request.method == 'POST':                                            
        form = EventForm(request.POST,instance=edetails)
        if form.is_valid():
            form.save()
            return redirect('inviter:dashboard')
        else:
            form = EventForm(instance=edetails)
        return render(request,'inviter/dashboard.html')

def edit_profile(request):
    eprofile = Inviter.objects.filter(username=request.session['username'])
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
            return redirect('inviter:dashboard')
        else:
            form = UserForm(instance=eprofile)
        return render(request,'inviter/dashboard.html')
    
def invitee_display(request):
    invitee = Invitee.objects.all()
    if request.GET.get('query'):
        query = request.GET.get('query','')
        invitee = invitee.filter(username__icontains=query)
    return render(request,{'invitee':invitee})
