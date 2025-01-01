from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.

def home(request):
    return render("home.html")

def register(request):
    if request.method == 'POST':
        form = inviter_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = inviter_form()
    return render(request,'register.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = invites_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = invites_form()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=user,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            er_msg = "Failed!"
            return render(request,'login.html', {'error':er_msg})
    return render(request,'login.html')


