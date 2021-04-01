from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, PasswordResetForm
from django.contrib.auth import authenticate, login ,logout
# Create your views here.

#login form
def Showform(request):
    if request.method == 'POST':
        sg=UserCreationForm(request.POST)

        if sg.is_valid():
            sg.save()
            
        else:
            sg=UserCreationForm()


            return render(request,'LoginForm/signup.html',{'form':sg})

#signup form

def sign_up(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')

            else:       
             fm=AuthenticationForm()


    return render(request,'login.html',{'show':fm})


#profile 
def user_profile(request):
    return render(request,'LoginForm/profile.html') 

#changepassword with old password

def user_change_pass(request):
    fm=PasswordChangeForm(user=request.user)
    return render(request,'LoginForm/changepass.html',{'form':fm})

#password reset

def pass_reset(request):
    fm=PasswordResetForm()
    return render(request,'LoginForm/resetpass.html',{'form':fm})    
    





