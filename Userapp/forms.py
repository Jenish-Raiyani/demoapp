from django import forms
from .models import Post
from django.contrib.auth.models import User

 

class UserRegistrationForm(forms.ModelForm):
     
    password = forms.CharField(widget=forms.PasswordInput())
    

    class Meta:
        model = Post
        fields = ["first_name","last_name", "email","username",  "password"]
