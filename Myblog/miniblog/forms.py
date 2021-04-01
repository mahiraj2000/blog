from django import forms

class SignUpForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    mobile=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)

