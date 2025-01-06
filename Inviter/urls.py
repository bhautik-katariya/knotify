from django.urls import path
from . import views

app_name = 'inviter'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add, name='add'),
    
   
] 