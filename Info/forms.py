

import django
from .models import Student_Data
from django import forms
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student_Data

        fields='__all__'

class UserForm(forms.ModelForm):
    class meta:
        model=User
        Fields=['Username','email','password']


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}))
    gender = forms.ChoiceField(choices=Student_Data.gender_choices, required=False)
    country = forms.ChoiceField(choices=Student_Data.country_choices, required=False)
