from django.db import models

# Create your models here.

class Invitee(models.Model):
    username = models.CharField(max_length=100,unique=True)
    f_name = models.CharField(max_length=100, verbose_name='First name') 
    l_name = models.CharField(max_length=100, verbose_name='Last name')    
    email = models.EmailField(unique=True)  
    phone_no = models.CharField(max_length=15) 
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        verbose_name = "Invitee"

    def __str__(self):
        return self.name 