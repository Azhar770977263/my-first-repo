from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.show_students, name='show_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('students/query/gpa_asc/', views.get_students_ordered_by_gpa, name='get_students_gpa_asc'),
    path('students/query/gpa_desc/', views.get_students_ordered_by_gpa_desc, name='get_students_gpa_desc'),
    path('students/query/name_contains_a/', views.get_students_with_name_a, name='get_students_with_name_a'),
    path('students/query/gpa_range/', views.get_students_with_gpa_range, name='get_students_with_gpa_range'),
    path('students/query/exact_gpa/', views.get_students_with_exact_gpa, name='get_students_with_exact_gpa'),
    path('students/query/exclude_name_age/', views.get_students_exclude_name_age, name='get_students_exclude_name_age'),
]