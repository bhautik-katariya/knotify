from django.urls import path
from .import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views=login_view,name='login'),
    path('inviter/',views=register_view,name='register'),
    path('invites/',views=register_view,name='register'),
    
     
]


