# users/urls.py
from django.urls import path
from .views import register_form, userlogin, userlogout, home,success_message

app_name = 'users'

urlpatterns = [
    path('register/', register_form, name='register'),
    path('', userlogin, name='login'),
    path('logout/', userlogout, name='logout'),
    path('home/', home, name='home'),
    path('success/', success_message, name='success'), 
]