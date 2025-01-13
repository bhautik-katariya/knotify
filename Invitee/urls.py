from django.urls import path
from . import views

app_name = 'invitee' 
urlpatterns = [
    path('', views.index, name='index'),
    path('date-event-list/<str:e_date>/', views.date_event_list, name='date_event_list'),
    path('event-detail/<int:event_id>/', views.event_details, name='event_details'),
]