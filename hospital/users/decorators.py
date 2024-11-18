from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from patients.models import Patients

from django.http import HttpResponse
from functools import wraps
def isadmin(view_fun):
    def wrapper_func(request,*args,**kwargs):
        if request.user.groups.exists:
            group=request.user.groups.all()[0].name
            print(group)
            if group=='admin':
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('401 Unauthorized')
        else:
            return HttpResponse('401 Unauthorized')
    return wrapper_func



def islogin(view_fun):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return view_func(request,*args,**kwargs)
            
    return wrapper_func
