from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Anand'})

def add(request):
    res=int(request.GET['num1'])+int(request.GET['num2'])
    return render(request,'result.html',{'result':res})    