from django.urls import path
from . import views

app_name = 'inviter'
urlpatterns = [
    path('', views.index, name='index'),
   
] 