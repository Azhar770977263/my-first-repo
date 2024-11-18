# users/models.py
#from django.contrib.auth.models import AbstractUser
#from django.db import models

#class User(models.Model):
    #username=models.CharField((""),max_length=50)
   # password1=models.CharField((""),max_length=50)
  #  password2=models.CharField((""),max_length=50)
 #   email = models.EmailField(unique=True)  # تأكد من أن البريد الإلكتروني فريد



 # users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # أضف related_name لتجنب التعارض
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # تغيير اسم العلاقة العكسية
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # تغيير اسم العلاقة العكسية
        blank=True,
    )

    def __str__(self):
        return self.username