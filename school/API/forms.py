from django  import forms
class StudentRegistrations(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()