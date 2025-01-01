from django.db import models

# Create your models here.

class Inviter(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name 
    
class Invites(models.Model):
    guest_name = models.CharField(max_length=100)  
    guest_email = models.EmailField(blank=True, null=True) 
    password = models.CharField(max_length=100)
    guest_no = models.CharField(max_length=15, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"Invites for {self.guest_name}" 
    
    
    