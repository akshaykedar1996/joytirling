from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subadmin_user

@admin.register(Subadmin_user)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subadmin_user._meta.fields]
