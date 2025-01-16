from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from Invitee.models import *
from Inviter.models import *
from django.contrib.auth.hashers import check_password


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

class Login(View):
    template_name = 'login.html'
    
    def get(self,request):
        form = LoginForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_role = form.cleaned_data['user_role']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = None
            if user_role == 'invitee':
                try:
                    user = Invitee.objects.get(username=username)
                except Invitee.DoesNotExist:
                    form.add_error('username', 'Invalid username')
            elif user_role == 'inviter':
                try:
                    user = Inviter.objects.get(username=username)
                except Inviter.DoesNotExist:
                    form.add_error('username', 'Invalid username')
            elif user_role == 'admin':
                if username == 'admin' and password == '12345':
                    request.session['username'] == username
                    return redirect('admin')
                else:
                    form.add_error(None, 'Invalid username/password')
            else: 
                form.add_error('user_role','select any one role')

            if user:
                if check_password(password, user.password):
                    if user_role == 'invitee': 
                        request.session['user_role'] = user_role                                            
                        request.session['username'] = username
                        return redirect('invitee:index')
                    elif user_role == 'inviter':
                        request.session['user_role'] = user_role
                        request.session['username'] = username
                        return redirect('inviter:dashboard')
                else:
                    form.add_error('password', 'Invalid password')
        return render(request, self.template_name, {'form': form})
    

def edit_profile(request, username):
    user_role = request.session['user_role']
    username = request.session['username']

    if user_role == 'inviter':
        eprofile = Inviter.objects.get(username=username)
    elif user_role == 'invitee':
        eprofile = Invitee.objects.get(username=username)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request=request)
        if form.is_valid():
            # Update eprofile fields
            eprofile.username = form.cleaned_data['username']
            eprofile.f_name = form.cleaned_data['f_name']
            eprofile.l_name = form.cleaned_data['l_name']
            eprofile.email = form.cleaned_data['email']
            eprofile.phone_no = form.cleaned_data['phone_no']
            try:
                eprofile.save()
                request.session['username'] = eprofile.username
            except Exception as e:
                print('Error saving profile:', e)

            if user_role == 'inviter':
                return redirect('inviter:dashboard')
            elif user_role == 'invitee':
                return redirect('invitee:index')
        else:
            print('Form is invalid:', form.errors)  # Debug form errors
    else:
        # Manually set initial data
        initial_data = {
            'username': eprofile.username,
            'f_name': eprofile.f_name,
            'l_name': eprofile.l_name,
            'email': eprofile.email,
            'phone_no': eprofile.phone_no,
        }
        form = ProfileForm(initial=initial_data, request=request)

    return render(request, 'edit_profile.html', {'form': form})

def logout(request):
    request.session.flush() # delete session and cookie and create empty session
    return redirect('login')

def admin(request):
    invitee = Invitee.objects.all() 
    inviter = Inviter.objects.all()
    events = EventDetails.objects.all()
    
    context = {
        'invitee':invitee,
        'inviter':inviter,
        'events':events
    }
    return render(request, 'admin.html', context)
