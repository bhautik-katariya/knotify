from django.urls import path
from . import views

app_name = 'invitee'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
   
] 