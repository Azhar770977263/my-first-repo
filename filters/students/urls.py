from django.urls import path
from . import views

urlpatterns=[
    path('edit_student/',views.edit_student,name="edit"),
    path('add_student/',views.add_student,name="add"),
    path('delete_student/',views.delete_student,name="delete"),
    path('get_student/',views.get_student,name="get"),
]