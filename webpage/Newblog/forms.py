from django import forms

class UserRegistration(forms.Form):
    comment=forms.CharField(widget=forms.Textarea)
    post=forms.CharField(widget=forms.Textarea)


class UserAdd(forms.Form):
        name=forms.CharField()
        email=forms.CharField()
        mobile=forms.IntegerField()
        password=forms.CharField(widget=forms.PasswordInput)
        rpassword=forms.CharField(label='password(again)', widget=forms.PasswordInput)



        def clean(self):
            cleaned_data=super().clean()
            valpwd=cleaned_data[password]
            valrpwd=cleaned_data[rpassword]
            if valpwd != valrpwd:
                raise form.validationError('password Does Not Matched')

  