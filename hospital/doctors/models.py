from django.db import models

class Doctors(models.Model):
    first_name = models.CharField(max_length=100,default='Unknown')
    last_name = models.CharField(max_length=100,default='Unknown')
    specialization = models.CharField(max_length=100,default='Unknown')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, default='example@example.com')  # إضافة قيمة افتراضية هنا
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"