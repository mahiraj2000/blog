from django.shortcuts import render
from .forms import StudentRegistrations
# Create your views here.

def showformdata(request):
    fm= StudentRegistrations()
    return render(request,'API/home.html',{'form':fm})