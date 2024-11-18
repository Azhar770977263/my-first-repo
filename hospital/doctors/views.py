from django.shortcuts import render, get_object_or_404, redirect
from .forms import DoctorsForm
from .models import Doctors
from django.urls import reverse
from django.db import IntegrityError
import os

# Create your views here.
def doctor_home(request):
    return render(request, 'doctor_home.html')

def doctor_list(request):
    doctors = Doctors.objects.all()
    if doctors.exists():
        return render(request, 'doctor_list.html', {'Doctors': doctors})
    else:
        return redirect(reverse('doctors:error_page'))

def success_messages(request):
    return render(request, 'success_messages.html')

def error_pages(request):
    return render(request, 'error_pages.html')

def doctor_show_detail(request, pk):
    doctor = get_object_or_404(Doctors, id=pk)
    return render(request, 'doctor_show_detail.html', {'doctors': doctor})

def doctor_delete(request, pk):
    try:
        doctor = get_object_or_404(Doctors, pk=pk)
        if doctor.image:
            image_path = doctor.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
        doctor.delete()
        return redirect(reverse('doctors:success_messages'))
    except Exception:
        return redirect(reverse('doctors:error_page'))

def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctors, id=pk)
    if request.method == 'POST':
        try:
            doctor.first_name = request.POST.get('fname')
            doctor.last_name = request.POST.get('lname')  # Corrected the name
            doctor.specialization = request.POST.get('specialization')  # Added specialization
            doctor.phone_number = request.POST.get('phone_number')  # Added phone number
            doctor.email = request.POST.get('email')  # Added email
            doctor.image = request.FILES.get('image')
            doctor.save()
            return redirect(reverse('doctors:success_messages'))
        except IntegrityError:
            return redirect(reverse('doctors:error_page'))
    else:
        return render(request, 'doctor_edit.html', {'doctors': doctor})

def doctor_create(request):
    if request.method == 'POST':
        try:
            doctor = Doctors.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                specialization=request.POST.get('specialization'),  # Added specialization
                phone_number=request.POST.get('phone_number'),  # Added phone number
                email=request.POST.get('email'),  # Added email
                image=request.FILES.get('image'),
            )
            return redirect(reverse('doctors:success_messages'))
        except IntegrityError:
            return redirect(reverse('doctors:error_page'))
    else:
        return render(request, 'doctor_create.html')

def show_forms(request):
    if request.method == 'POST':
        doctor_form = DoctorsForm(request.POST, request.FILES)
        if doctor_form.is_valid():
            doctor_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!!')
    else:
        doctor_form = DoctorsForm()
        return render(request, 'other_type_forms.html', {'form': doctor_form})