from django.contrib import admin
from .models import Data
from .models import SecondData
# Register your models here.
@admin.register(Data)
class UserAdmin(admin.ModelAdmin):
    list_display=('Post','Comment')

@admin.register(SecondData)
class ForUser(admin.ModelAdmin):
    list_display=('name','email','mobile','password','rpassword')




