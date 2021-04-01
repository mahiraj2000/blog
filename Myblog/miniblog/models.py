from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()

class SignUpData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    rpassword=models.CharField(max_length=50)

class LoginData(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    



