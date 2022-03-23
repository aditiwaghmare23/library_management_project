import imp
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Book(models.Model):
    book_name=models.CharField(max_length=30,null=True)
    author_name=models.CharField(max_length=30,null=True)
    pub_date=models.DateField()
    return_date=models.DateField()
    cost=models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.book_name

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)

    def __str__(self):
        return self.name