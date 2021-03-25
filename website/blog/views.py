from django.shortcuts import render
from .forms import UserRegistration
from .forms import ForRegister
# Create your views here.
from .models import Data
def showform(request):
  #  if request.method == 'POST'
    sh = UserRegistration(request.POST)
    if sh.is_valid():

        
        ps=sh.cleaned_data['Post']
        cs=sh.cleaned_data['Comment']
        reg=Data(Post=ps,Comment=cs)
        reg.save()
        

    else:
        
          sh=UserRegistration()
    return render(request,'blog/home.html',{'form':sh})


def register(request):
   # if request.method. == 'POST'
    re=ForRegister(request.POST)
    if re.is_valid():

        nm=re.cleaned_data['name']
        em=re.cleaned_data['email']
        mn=re.cleaned_data['mobile']
        ps=re.cleaned_data['password']
        rs=re.cleaned_data['rpassword']

        fer=SecondData(name=nm,email=em,mobile=mn,password=ps,rpassword=rs)


    else:
        re=ForRegister()

        return render(request,'blog/register.html',{'regi':re})    

        



        









