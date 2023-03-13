from django.contrib import admin
from .models import UserManagement

# Register your models here.
@admin.register(UserManagement)
class Admin_UserManagement(admin.ModelAdmin):
    list_display = ['id','ps','firstname','lastname','email','gender','phone','role','status']