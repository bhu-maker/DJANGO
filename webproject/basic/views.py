from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,request
from urllib import response

# Create your views here.
def func1(request):
    return HttpResponse("<h1> welcome to django</h1>")

def func2(request):
    return render(request,'htmlfile.html')

def func3(request):
    return render(request,'htmlfile2.html',{"data":"gud morning"})


