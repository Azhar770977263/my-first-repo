from django.urls import path
from . import views

urlpatterns=[

 

    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('show/',views.showstudent,name="showstudent"),
    path('edit/',views.editstudent,name="edit"),
    path('delete/',views.deletestudent,name="delete"),
    
]