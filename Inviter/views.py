from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Knotify.forms import *

# Create your views here.

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)  
        if form.is_valid():
            # data = {
            #     'username':request.session['username'],
            #     'e_name':form.cleaned_data['e_name'],
            #     'g_name':form.cleaned_data['g_name'],
            #     'b_name':form.cleaned_data['b_name'],
            #     'e_date':form.cleaned_data['e_date'],
            #     'place':form.cleaned_data['place'], 
            # }
            # EventDetails.objects.create(**data)
            event = form.save(commit=False)
            event.username = request.session['username']
            event.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request,{'form':form})

def event_list(request):
    events = EventDetails.objects.all()
    return render(request,{'events':events})

def dashboard(request):
    return render(request,'inviter/dashboard.html')

def event_update(request,id): 
    edetails = EventDetails.objects.get(id = id)
    if request.method == 'POST':                                            
        form = EventForm(request.POST,instance=edetails)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
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
            return redirect('dashboard')
        else:
            form = UserForm(instance=eprofile)
        return render(request,'inviter/dashboard.html')
    
def invitee_display(request):
    invitee = Invitee.objects.all()
    if request.GET.get('query'):
        query = request.GET.get('query','')
        invitee = invitee.filter(username__icontains=query)
    return render(request,{'invitee':invitee})
