from django.contrib import admin
from .models import Post, SignUpData, LoginData
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']


@admin.register(SignUpData)
class SignUpDataAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','mobile','email','password','rpassword']    

@admin.register(LoginData)
class LoginDataAdmin(admin.ModelAdmin):
    list_display=('username','password')
