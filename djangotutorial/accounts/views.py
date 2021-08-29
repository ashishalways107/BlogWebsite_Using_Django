from django import forms
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . import forms
# Create your views here.

def register(request):
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data["username"]
            password1=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.info(request,'User Created')
            return redirect('login')
        else:
            messages.info(request,form.errors)
            return redirect('register')     
    else:
        form=forms.FormName()
        return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')    
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)     
    return redirect('/')   