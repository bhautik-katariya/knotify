import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render,redirect
from django.http import Http404
from datetime import datetime
from .models import *
from Knotify.forms import *
from Inviter.models import *

# Create your views here.

folder = 'invitee/'

def index(request):
    username = request.session['username']
    invitee = Invitee.objects.get(username=username)  # Get Invitee object by username
    events = EventDetails.objects.filter(invitee=invitee)  # Filter events based on the Invitee object
    event_dates = {e.e_date.strftime('%Y-%m-%d'): True for e in events}  # Serialize the event dates
    return render(request, 'invitee/calendar.html', {'event_dates': json.dumps(event_dates, cls=DjangoJSONEncoder), 'username':username})

def date_event_list(request, e_date):
    username = request.session['username']
    invitee = Invitee.objects.get(username=username)
    date_obj = datetime.strptime(e_date, '%Y-%m-%d')
    events = EventDetails.objects.filter(invitee=invitee, e_date__date=date_obj.date())
    # if not events:
    #     raise Http404("No events found")
    return render(request,'invitee/date_event_list.html', {'events': events, 'date': e_date})

def event_details(request, event_id):
    event = EventDetails.objects.get(pk=event_id)
    return render(request, 'invitee/event_details.html',{'event':event})
