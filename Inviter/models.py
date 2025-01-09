from django.db import models
from Invitee.models import *

# Create your models here.

class Inviter(models.Model):
    username = models.CharField(max_length=100,unique=True)
    f_name = models.CharField(max_length=100, verbose_name='First name') 
    l_name = models.CharField(max_length=100, verbose_name='Last name')   
    email = models.EmailField(unique=True) 
    phone_no = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        verbose_name = 'Inviter'
        
    def __str__(self):
        return self.username
     
class EventDetails(models.Model):
    inviter = models.ForeignKey(Inviter,on_delete=models.CASCADE)
    e_name = models.CharField(max_length=100,verbose_name='Event Name')
    g_name = models.CharField(max_length=50,verbose_name='Groom Name')
    b_name = models.CharField(max_length=50,verbose_name='Bride Name')
    e_date = models.DateTimeField(verbose_name='Event Date')
    place = models.CharField(max_length=500)
    invitee = models.ManyToManyField(Invitee, related_name='event')
    
    class Meta:
        verbose_name = 'Event Details'
        
    def __str__(self):
        return f'{self.inviter.username} {self.e_name}'