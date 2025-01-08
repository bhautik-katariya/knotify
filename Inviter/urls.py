from django.urls import path
from . import views

app_name = 'inviter'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_event, name='add'),
    path('update/',views.event_update,name='update'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('invitee_display/',views.invitee_display,name='invitee_display'),
    
] 