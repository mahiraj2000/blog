from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
class SignUpForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    mobile=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    #password= forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplate':'current-password', 'class':'form-control'}))
    password=forms.CharField()

class PostComment(forms.Form):
    comment=forms.CharField(widget=forms.TextInput)
    post=forms.CharField(widget=forms.Textarea)

    
