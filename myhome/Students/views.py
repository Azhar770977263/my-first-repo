from django.shortcuts import render

# from Students.filters import StudentsFilters
from . models import Students
from django.http import HttpResponse
from django.db.models import Q
# import django_filters # type: ignore
# from django_filters import FilterView 
# Create your views here.

# class StudentsListView(FilterView):
#     model =Students
#     filterset_class = StudentsFilters
#     template_name='showstudents.html'

# الصفحة الأساسية 
def index(request):
    return render(request,'index.html')
# صفحة العرض
def showstudents(request):
    return render(request,'showstudents.html')
    
# صفحة الحذف
def editstudents(request):
    return render(request,'editstudents.html')


# تعديل طالب
def deletestudents(request):
    return render(request,'deletestudents.html')

# تعديل طالب
def edit_students(request,pk):
    students=Students.objects.get(pk=pk)
    # students=Students.objects.get(l_name=pk)
    students.Levels=4
    students.l_name="rasha"
    students.save()
    return HttpResponse("Update Done")

# حذف طالب
def delete_students(request,pk):
    students=Students.objects.get(pk=pk)
    students.delete()
    return HttpResponse("Delete Done")


def getstudents(request):
    students=Students.objects.all()
    count= Students.objects.all().count()
    # return HttpResponse("Get Done")
    return render(request,'showstudents.html',{"students":students})

# اضافة طالب
def add_students(reguest):
    Students.objects.create(
        f_name="azhar",
        l_name="adel",
        age=22,
        gpa=80.3,
        statust=True,
        reporet="Normal",
        level='4',
    ).save()
    return HttpResponse("Add Done")

# عرض الطالب الذي في اسمه حرف r
def getstudentss(request):
    students=Students.objects.filter(f_name__contains='a')
    return render(request,'showstudents.html',{"students":students})
    
#تصاعديا   
def getstudent(request):
    students=Students.objects.all().order_by('gpa')
    return render(request,'showstudents.html',{"students":students})
    # return HttpResponse("get Done")

# عرض الطلاب مرتبين على حسب gpa تنازليا   
# def getstudent(request):
#     students=Students.objects.all().order_by('-gpa')
#     return render(request,'showstudents.html',{"students":students})
#     # return HttpResponse("get Done")

def getstudentna(request):
    students=Students.objects.filter(gpa__range=[87,90])
    return render(request,'showstudents.html',{"students":students})


def getstudentnac(request):
    students=Students.objects.filter(gpa__exact=90)
    return render(request,'showstudents.html',{"students":students})


def getstudentnacr(request):
    students=Students.objects.all().exclude(f_name="azhar")
    return render(request,'showstudents.html',{"students":students})

def getif(request):
    students=Students.objects.all().exclude(Q(f_name="adel")|Q(age=22))
    return render(request,'showstudents.html',{"students":students})

