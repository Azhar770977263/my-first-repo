# users/admin.py
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)

# تسجيل النموذج مع الإدارة
admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.site_header='H.P.S'
#admin.site.site_title='H.P.S'
#admin.site.register(User)

