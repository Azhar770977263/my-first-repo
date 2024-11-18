from django.urls import path
from . import views

urlpatterns=[

    path('',views.homes,name="homes"),
    path('show/',views.showteacher,name="show"),
    path('edit/',views.editteacher,name="edit"),
    path('delete/',views.deleteteacher,name="delete"),
    
]