from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostComment
from .models import SignUpData, LoginData 
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
    if request.method == "POST":
        
        form=SignUpForm(request.POST)
        
        if form.is_valid():
            fm=form.clean_data['first_name']
            lm=form.cleaned_data['last_name']
            mb=form.cleaned_data['mobile']
            em=form.cleaned_data['email']
            ps=form.cleaned_data['password']
            rps=form.cleaned_data['rpassword']
            datasave= SignUpData(first_name=fm,last_name=lm,mobile=mb,email=em,password=ps,rpassword=rps)
            datasave.save()
            

    else:

        form=SignUpForm()
    return render(request,'miniblog/signup.html',{'form':form})

#login
def user_login(request):
    if request.method == 'POST':
       form =LoginForm(request.POST)
       if form.is_valid():
           us=form.cleaned_data['username']
           ps=form.cleaned_data['password']
           loginsave=LoginData(username=us,password=ps)
           loginsave.save()

    else:
        form=LoginForm()
        return render(request,'miniblog/login.html',{'form':form})    


#For Post and Comment
def user_post(request):
    form= PostComment()
    return render(request,'miniblog/posts.html',{'form':form})

