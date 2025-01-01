from django.contrib import admin
from .models import Inviter,Invites

# Register your models here.
admin.site.register(Inviter,Invites)