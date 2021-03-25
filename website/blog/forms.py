from django import forms


class UserRegistration(forms.Form):
     
     Post=forms.CharField(widget=forms.Textarea)
     Comment=forms.CharField(widget=forms.Textarea)
     """ mobile=forms.IntegerField()
     email=forms.EmailField()
     password=forms.CharField(widget=forms.PasswordInput)
     rpassword=forms.CharField(label='password again',widget=forms.PasswordInput)"""


class ForRegister():
     name=forms.CharField()
     email=forms.EmailField()
     mobile=forms.IntegerField()
     password=forms.CharField(widget=forms.PasswordInput)
     rpassword=forms.CharField(label='password(again)', widget=forms.PasswordInput)

     def clean(self):
          clean_data=super().clean()
          valpwd=clean_data[password]
          valrpwd=clean_data[password]
          if valpwd != valrpwd:
               raise forms.ValidationError('Password Does Not Matched')
