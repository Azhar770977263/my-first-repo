from django.urls import path
from . import views

urlpatterns=[

    path('delete/',views.deletestudents,name="delete"),
    ]
