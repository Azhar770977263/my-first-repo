from django.urls import path
from . import views


app_name='doctors'
urlpatterns = [
  path('',views.doctor_home,name='home'),
    
    

 #path('index/',views.index,name='index'),
  path('doctor_create/',views.doctor_create,name='create'),

  path('doctor_list/',views.doctor_list,name='show'),

    
  path('success_messages/',views.success_messages,name ='success_messages'),

  path('error_pages/',views.error_pages,name='error_page'),

  path('doctor_show_detail/<int:pk>',views.doctor_show_detail,name='showdetail'),

  path('doctor_edit/<int:pk>',views.doctor_edit,name='edit'),


  
  path('doctor_delete/<int:pk>',views.doctor_delete,name='delete'),


  path('show_forms/',views.show_forms,name='forms'),



    
]
    
