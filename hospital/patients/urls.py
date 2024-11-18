from django.urls import include, path
from . import views

app_name='patients'
urlpatterns= [
    path('',views.home,name='home'),
    path('create/',views.patients_create,name='create'),
    path('show/',views.patients_list,name='show'),
    path('success/',views.success_message,name='success_message'),
    path('error/',views.error_page,name='error_page'),
    path('showdetail/<int:pk>',views.patients_show_detail,name='showdetail'),
   # path('showdetail/<int:id>/', views.patients_show_detail, name='showdetail'),
    path('update/<int:pk>',views.patient_edit,name='edit'),
    path('delete/<int:pk>',views.patient_delete,name='delete'),
    path('forms/',views.show_form,name='forms'),
]