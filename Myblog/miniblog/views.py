from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.
#HOME 
def home(request):
    return render(request,'miniblog/homes.html')

#ABOUT
def about(request):
    return render(request,'miniblog/abouts.html')

#Contact
def contact(request):
    return render(request,'miniblog/contact.html')

#Logout
def user_logout(request):
    return HttpResponseRedirect('/')

#signup
def use_signup(request):
    form=SignUpForm()
    return render(request,'miniblog/signup.html',{'form':form})

#login
def user_login(request):
    return render(request,'miniblog/login.html')    
