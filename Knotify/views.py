from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from Invitee.models import *
from Inviter.models import *
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, 'inviter/dashboard.html')

class Login(View):
    template_name = 'login.html'
    
    def get(self,request):
        form = LoginForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['user_role']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = None
            if role == 'invitee':
                try:
                    user = Invitee.objects.get(username=username)
                except Invitee.DoesNotExist:
                    form.add_error('username', 'Invalid username')
            elif role == 'inviter':
                try:
                    user = Inviter.objects.get(username=username)
                except Inviter.DoesNotExist:
                    form.add_error('username', 'Invalid username')
            else: 
                form.add_error('user_role','select any one role')

            if user:
                if check_password(password, user.password):
                    if role == 'invitee':                                               
                        request.session['username'] = username
                        return redirect('invitee:index')
                    elif role == 'inviter':
                        request.session['username'] = username
                        return redirect('inviter:dashboard')
                else:
                    form.add_error('password', 'Invalid password')

        return render(request, self.template_name, {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_role = form.cleaned_data['user_role']
            data = {
                'username':form.cleaned_data['username'],
                'f_name':form.cleaned_data['f_name'],
                'l_name':form.cleaned_data['l_name'],
                'email':form.cleaned_data['email'],
                'phone_no':form.cleaned_data['phone_no'],
                'password':form.cleaned_data['password']
            }
            
            if user_role == 'invitee':
                Invitee.objects.create(**data)
                return redirect('login')
            elif user_role == 'inviter':
                Inviter.objects.create(**data)
                return redirect('login')
            else:
                form.add_error('user_role', 'Select any one of these')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})

def logout(request):
    request.session.flush() # delete session and cookie and create empty session
    # del request.session['username'] # deletes specific session key
    return redirect('login')