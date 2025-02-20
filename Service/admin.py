from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Service.models import service
# Register your models here.
@admin.register(service)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in service._meta.fields] 