import django_filters
from .models import Students

from . import models
from . models import*

from django_filters import Filter

#class StudentFilter(Filter):

 #   class meta:
  #      model=Students
   #     field='__all__'



class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Students
        fields = {
            'f_name': ['icontains'],  # فلترة الاسم الأول
            'l_name': ['icontains'],  # فلترة الاسم الأخير
            'age': ['exact', 'lt', 'gt'],  # فلترة العمر
            'gpa': ['exact', 'lt', 'gt'],  # فلترة GPA
            'level': ['exact'],  # فلترة المستوى
        }        