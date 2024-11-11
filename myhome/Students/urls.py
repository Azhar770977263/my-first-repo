from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('showstudents',views.showstudents,name='showstudents'),
    path('editstudents',views.editstudents,name='editstudents'),
    path('deletestudents',views.deletestudents,name='deletestudents'),
    path('getstudents',views.getstudents,name='getstudents'),
    path('edit_students',views.edit_students,name='edit_students'),
    path('delete_students/<int:pk>/',views.delete_students,name='delete_students'),
    path('add_students',views.add_students,name='add_students'),
    path('getstudent',views.getstudent,name='getstudent'),
    path('getstudentss',views.getstudentss,name='getstudentss'),
    path('getstudentna',views.getstudentna,name='getstudentna'),
    path('getstudentnac',views.getstudentnac,name='getstudentnac'),
    path('getstudentnacr',views.getstudentnacr,name='getstudentnacr'),
    path('getif',views.getif,name='getif'),

]