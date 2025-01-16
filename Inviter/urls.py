from django.urls import path
from . import views

app_name = 'inviter' 
urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('add-event/', views.add_event, name='add_event'), 
    path('update-event/<int:event_id>/', views.event_update, name='event_update'), 
] 