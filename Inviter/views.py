from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import View       
from django.http import HttpResponse

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)  
        if form.is_valid():
            data = {
                'username':request.session['username'],
                'e_name':form.cleaned_data['e_name'],
                'g_name':form.cleaned_data['g_name'],
                'b_name':form.cleaned_data['b_name'],
                'e_date':form.cleaned_data['e_date'],
                'place':form.cleaned_data['place'], 
            }
            EventDetails.objects.create(**data)
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request,{'form':form})

def event_list(request):
    events = EventDetails.objects.all()
    return render(request,{'events':events})

def dashboard(request):
    return render(request,'inviter/dashboard.html')
