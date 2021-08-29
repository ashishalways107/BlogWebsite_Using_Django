from django import forms
from django.core import validators
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
class FormName(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    username=forms.CharField(max_length=20)
    email=forms.EmailField(max_length = 100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        username=all_clean_data['username']
        email=all_clean_data['email']
        password=all_clean_data['password']
        confirm_password=all_clean_data['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Username Taken")
            elif User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email Taken")
        else:
            raise forms.ValidationError("Invalid Credentials.....")