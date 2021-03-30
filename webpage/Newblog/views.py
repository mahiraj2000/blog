from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration
from .forms import UserAdd
# Create your views here.
from .models import CommentData
from .models import RegisterData 

def showform(request):
    if request.method == 'POST':
        fm=UserRegistration(request.POST)
        if fm.is_valid():

            cm=fm.cleaned_data['comment']
        ps=fm.cleaned_data['post']
        reg=CommentData(comment=cm,post=ps)
        reg.save()

    else:
            fm=UserRegistration()

    return render(request,'Newblog/home.html',{'forms':fm})

def showData(request):
    if request.method =='POST':


        sh= UserAdd(request.POST)
        if sh.is_valid():


          nm=sh.cleaned_data['name']
          em=sh.cleaned_data['email']
          mb=sh.cleaned_data['mobile']
          ps=sh.cleaned_data['password']
          rs=sh.cleaned_data['rpassword']

        fer= RegisterData(name=nm,email=em,mobile=mb,password=ps,rpassword=rs)
        fer.save()
    else:
        sh=UserAdd()

        return render(request,'Newblog/register',{'show':sh})


#UserCreationsForm
def sign_up(request):
    up=UserCreationForm()
    return render(request,'Newblog/signup.html',{'sign':up})

