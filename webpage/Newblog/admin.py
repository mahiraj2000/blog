from django.contrib import admin
from .models import CommentData
from .models import RegisterData

# Register your models here.
@admin.register(CommentData)
class UserComment(admin.ModelAdmin):
    list_display=('comment','post')

@admin.register(RegisterData,)
class ForRegister(admin.ModelAdmin):
    list_display=('name','email','mobile','password','rpassword')    


