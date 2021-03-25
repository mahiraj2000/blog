from django.db import models

# Create your models here.
class Data(models.Model):
    Post=models.CharField(max_length=50)
    Comment=models.CharField(max_length=50)

class SecondData(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField(max_length=50)
     mobile=models.IntegerField()
     password=models.CharField(max_length=50)
     rpassword=models.CharField(max_length=50)



