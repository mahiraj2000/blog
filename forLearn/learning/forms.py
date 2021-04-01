from django import forms

class Form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
