from django.urls import reverse
import os
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PatientsForm
from .models import Patients

# Create your views here.

def home(request):
    return render(request,'patients_home.html')

#داله لعرض كل البيانات في صفحة العرض

def patients_list(request):
    patients = Patients.objects.all()
    if patients.exists():
        return render(request, 'patients_list.html', {'Patients': patients})  # تأكد من كتابة الحرف الكبير في 'Patients'
    else:
        return redirect(reverse('patients:error_page'))   
#success
def success_message(request):
    return render(request,'success_message.html')

#error
def error_page(request):
    return render(request,'error_page.html')

#عرض بيانات المريض الواحد
#def patient_show_detail(requset, pk):
 #   patient=Patients.objects.filter(id=pk)[0]
  #  try:
   #     return render(requset,'patients_info.html',{'patient':patient})
    #except:
     #   return redirect(reverse('patients:error_page'))




# patients/views.py
def patients_show_detail(request, pk):  # استخدم 'pk' هنا
    patient = get_object_or_404(Patients, id=pk)
    return render(request, 'patients_info.html', {'patient': patient})

import os
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Patients  # تأكد من استخدام النموذج الصحيح

def patient_delete(request, pk):
    try:
        # استرجاع المريض باستخدام pk
        patient = get_object_or_404(Patients, pk=pk)  # تأكد من استخدام Patients بدلاً من Doctors

        # حذف الصورة إذا كانت موجودة
        if patient.image:
            image_path = patient.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)  # حذف الصورة من النظام

        # حذف المريض
        patient.delete()  # حذف المريض من قاعدة البيانات
        
        # إعادة التوجيه إلى صفحة النجاح
        return redirect(reverse('patients:success_message'))
    
    except Exception as e:
        print(f"Error occurred while deleting patient: {e}")  # طباعة الخطأ في السجل
        return redirect(reverse('patients:error_page'))  # إعادة التوجيه إلى صفحة الخطأ


def patients_create(request):
    if request.method == 'POST':
        try:
            patient= Patients.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                age=request.POST.get('age'),
                report=request.POST.get('report'),
                image=request.FILES.get('image'),
                files_report=request.FILES.get('medical_report')
            )
            return redirect(reverse('patients:success_message'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    else:
        return render(request, 'patients_create.html')
    

#
def show_form(request):
    if request.method == 'POST':
        patient_form = PatientsForm(request.POST, request.FILES)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!!')
    else:
        patient_form = PatientsForm()
        return render(request, 'other_type_forms.html', {'form': patient_form})

# patients/views.py
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db import IntegrityError
from .models import Patients

from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
import os

def patient_edit(request, pk):
    patient = get_object_or_404(Patients, id=pk)
    
    if request.method == 'POST':
        try:
            # تحديث بيانات المريض
            patient.first_name = request.POST.get('fname')
            patient.last_name = request.POST.get('lname')
            patient.age = request.POST.get('age')
            
            # تحقق مما إذا كانت هناك صورة جديدة
            new_image = request.FILES.get('image')
            if new_image:
                # حذف الصورة القديمة إذا كانت موجودة
                if patient.image and os.path.isfile(patient.image.path):
                    os.remove(patient.image.path)
                patient.image = new_image  # تعيين الصورة الجديدة

            # تحقق مما إذا كان هناك ملف جديد للتقرير الطبي
            new_file_report = request.FILES.get('medical_report')
            if new_file_report:
                patient.file_report = new_file_report
            
            # حفظ التغييرات
            patient.save()
            return redirect(reverse('patients:success_message'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    
    # إذا كان الطلب ليس POST، أعد عرض النموذج مع بيانات المريض الحالية
    return render(request, 'patients_update.html', {'patient': patient})