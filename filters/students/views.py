from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Students

from .filters import StudentFilter
from .models import *
#from .models import Students
# Create your views here.
#def get_student(request):
 #   students=Students.objects.all()
  #  count=Students.objects.all.count()
   # searchfilter=StudentFilter()
    #return render(request,'get_student.html',{"myfilter":searchfilter})




def get_student(request):
    students = Students.objects.all()
    
    # تطبيق الفلتر
    searchfilter = StudentFilter(request.GET, queryset=students)
    students = searchfilter.qs  # الحصول على النتائج المفلترة

    return render(request, 'get_student.html', {
        "myfilter": searchfilter,
        "students": students,  # تمرير قائمة الطلاب المفلترة
    })









def edit_student(request,pk):
    students=Students.objects.get(pk=pk)
    students.level=3
    students.l_name="aaaaaa"
    students.save()
    return HttpResponse("update done")


def delete_student(request,pk):
    students=Students.objects.get(pk=pk)
    students.delete()
    return HttpResponse("delete done")

def add_student(request):
    Students.objects.create(
        f_name="eeee",
        l_name="rrrr",
        age=22,
        gpa=99,
        reporet="repport1",
        level="4",
        statust="statust1",
        ).save()
    return HttpResponse("add done")



