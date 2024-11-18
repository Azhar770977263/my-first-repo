from django.shortcuts import render, get_object_or_404, redirect
from .models import Students
from django.http import HttpResponse

# الصفحة الأساسية 
def index(request):
    return render(request, 'index.html')

# صفحة عرض الطلاب
def show_students(request):
    students = Students.objects.all()
    return render(request, 'show_students.html', {"students": students})

# إضافة طالب
def add_student(request):
    if request.method == "POST":
        Students.objects.create(
            f_name=request.POST['f_name'],
            l_name=request.POST['l_name'],
            age=request.POST['age'],
            gpa=request.POST['gpa'],
            statust=request.POST['statust'] == 'on',
            reporet=request.POST['reporet'],
            level=request.POST['level'],
        )
        return redirect('show_students')
    return render(request, 'add_student.html')

# تعديل طالب
def edit_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        student.f_name = request.POST['f_name']
        student.l_name = request.POST['l_name']
        student.age = request.POST['age']
        student.gpa = request.POST['gpa']
        student.statust = request.POST['statust'] == 'on'
        student.reporet = request.POST['reporet']
        student.level = request.POST['level']
        student.save()
        return redirect('show_students')
    return render(request, 'edit_student.html', {"student": student})

# حذف طالب
def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    return redirect('show_students')

def get_students_ordered_by_gpa(request):
    students = Students.objects.all().order_by('gpa')
    return render(request, 'show_students.html', {"students": students})

def get_students_ordered_by_gpa_desc(request):
    students = Students.objects.all().order_by('-gpa')
    return render(request, 'show_students.html', {"students": students})

def get_students_with_name_a(request):
    students = Students.objects.filter(f_name__contains='a')
    return render(request, 'show_students.html', {"students": students})

def get_students_with_gpa_range(request):
    students = Students.objects.filter(gpa__range=[87, 90])
    return render(request, 'show_students.html', {"students": students})

def get_students_with_exact_gpa(request):
    students = Students.objects.filter(gpa__exact=90)
    return render(request, 'show_students.html', {"students": students})

def get_students_exclude_name_age(request):
    students = Students.objects.exclude(f_name="adel", age=22)
    return render(request, 'show_students.html', {"students": students})