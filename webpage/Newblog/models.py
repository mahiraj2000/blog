from django.db import models

# Create your models here.
class CommentData(models.Model):
    comment=models.CharField(max_length=50)
    post=models.CharField(max_length=50,default='not add')


class RegisterData(models.Model):
        name=models.CharField(max_length=50)
        email=models.EmailField(max_length=50)
        mobile=models.IntegerField()
        password=models.CharField(max_length=50)
        rpassword=models.CharField(max_length=50)











