from django import forms
from .models import Doctors

class DoctorsForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name", 
        widget=forms.TextInput(), 
        required=True, 
        initial='doctors', 
        help_text="This Is The First Name"
    )

    last_name = forms.CharField(
        label="Second Name", 
        widget=forms.TextInput(), 
        required=True, 
        initial='doctors', 
        help_text="This Is The Second Name"
    )

    specialization = forms.CharField(
        label="Specialization", 
        widget=forms.TextInput(), 
        required=True, 
        help_text="Enter your specialization"
    )

    phone_number = forms.CharField(
        label="Phone Number", 
        widget=forms.TextInput(), 
        required=True, 
        help_text="Enter your phone number"
    )

    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(), 
        required=True, 
        help_text="Enter your email address"
    )

    image = forms.ImageField(
        label="Image", 
        widget=forms.FileInput()
    )

    class Meta:
        model = Doctors
        fields = ['first_name', 'last_name', 
        'specialization', 'phone_number', 'email', 'image']