from django import forms
from .models import Patients

class PatientsForm(forms.ModelForm):
    first_name = forms.CharField(label="First name", widget=forms.TextInput(),required=True,initial='patients',help_text="This is the first name")
    last_name = forms.CharField(label="Last name", widget=forms.TextInput(),required=True,initial='patients',help_text="This is the last name")
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(),required=True,initial='18')
    image = forms.ImageField(label="Image", widget=forms.FileInput())
    file_report = forms.FileField(label="File report", widget=forms.FileInput())
    report = forms.CharField(label="Report", widget=forms.Textarea())

    class Meta:
        model = Patients
        fields = ['first_name', 'last_name', 'age', 'image', 'file_report', 'report']

#الطريقة الثالثة
# from django import forms
# from .models import Patients

# class PatientsForm(forms.ModelForm):
#     class Meta:
#         model = Patients
#         fields = ['first_name', 'last_name', 'age', 'report']