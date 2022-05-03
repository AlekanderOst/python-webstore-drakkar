from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email' ,required=True)
    username = forms.CharField(label='Name' ,required=True)
    password1 = forms.CharField(label='Password' ,required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password' ,required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']