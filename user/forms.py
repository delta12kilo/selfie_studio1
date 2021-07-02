from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import  User
from django.contrib.auth.forms import AuthenticationForm ,UsernameField
from django.forms.models import ModelForm
from django.utils.translation import gettext,gettext_lazy as _
from .models import UserProfile,Adderss
from django.forms import fields, widgets

class CustomerRegistrationForm(UserCreationForm):
    password1 =forms.CharField(label='Password',widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label='Confirm Password (again)',widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    email =forms.CharField(required=True,widget=forms.
    EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fields=['username','email','password1','password2']
        labels ={'email':'Email'}
        widgets ={'username':forms.TextInput(attrs={'class':'form-control'})}



class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),
         strip=False,widget=forms.TextInput(attrs={'autocomplete':'current-password','class':'form-control'}))









class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=['name','DOB','gender','phone','img']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'DOB':forms.TextInput(attrs={'class':'form-control'}),
        #'img':forms.TextInput(attrs={'class':'form-control'}),
        'gender':forms.TextInput(attrs={'class':'form-control'}),
      #  
        }

class AdderssForm(forms.ModelForm):
    """Form definition for Adderss."""

    class Meta:
        """Meta definition for Adderssform."""

        model = Adderss
        fields = ('add','state','city','zipcode')
        widgets={'state':forms.TextInput(attrs={'class':'form-control'}),
        'add':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'zipcode':forms.TextInput(attrs={'class':'form-control'})
        }



