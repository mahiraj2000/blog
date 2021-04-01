from django.contrib import admin
from .models import FormData
# Register your models here.
@admin.register(FormData)
class FormAdmin(admin.ModelAdmin):
    list_display=('username','password')