from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Knotify.forms import *

# Create your views here.

def dashboard(request):
    username=request.session['username']
    inviter = Inviter.objects.get(username=username)
    events = EventDetails.objects.filter(inviter=inviter)
    return render(request,'inviter/dashboard.html',{'events':events})

def add_event(request): 
    if request.method == 'POST':
        form = EventForm(request.POST)  
        if form.is_valid():
            # event = form.save(commit=False)
            username = request.session['username']
            inviter = Inviter.objects.get(username=username)
            e_name = request.POST['e_name']
            g_name = request.POST['g_name']
            b_name = request.POST['b_name']
            e_date = request.POST['e_date']
            place = request.POST['place']
            invitee = request.POST.getlist('invitee')
            event = EventDetails.objects.create(inviter=inviter, e_name=e_name, g_name=g_name, b_name=b_name, e_date=e_date, place=place)
            event.invitee.add(*Invitee.objects.filter(id__in=invitee))
            # event.inviter = inviter
            # event.save()
            return redirect('inviter:dashboard')
    else:
        form = EventForm()
    return render(request,'inviter/event_form.html',{'form':form})

# def event_update(request,id): 
#     edetails = EventDetails.objects.get(pk=id)
#     if request.method == 'POST':                                            
#         form = EventForm(request.POST,instance=edetails)
#         if form.is_valid():
#             form.save()
#             return redirect('inviter:dashboard')
#         else:
#             form = EventForm(instance=edetails)
#         return render(request,'inviter/dashboard.html')

    
# def invitee_display(request):
#     invitee = Invitee.objects.all()
#     if request.GET.get('query'):
#         query = request.GET.get('query','')
#         invitee = invitee.filter(username__icontains=query)
#     return render(request,{'invitee':invitee})
