# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import CustomUser 
from .decorators import islogin, isadmin
 # استخدام النموذج المخصص هنا

def register_form(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User {username} created successfully")
            return redirect('users:login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    
    context = {'form': form}
    return render(request, 'register_form.html', context)


@isadmin
def patients_create(request):
    if request.method == 'POST':
        try:
            patient = Patients.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                age=request.POST.get('age'),
                report=request.POST.get('report'),
                image=request.FILES.get('image'),
                files_report=request.FILES.get('medicalreport')
            )
            return redirect(reverse('patients:success_message'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    else:
        return render(request, 'patients/patients_create.html')
    


def userlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(email=email)
            username = user.username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:success')  # توجيه إلى صفحة النجاح
            else:
                messages.error(request, "Invalid username or password")
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid email or password")
    
    return render(request, 'login_form.html')

def userlogout(request):
    logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def home(request):
    return render(request, 'home.html')  # صفحة home

# رسالة نجاح
def success_message(request):
    app_name = 'users'
    return render(request, 'success_message.html', {'app_name': app_name})