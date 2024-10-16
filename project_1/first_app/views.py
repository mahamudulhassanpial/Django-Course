from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("this is first app/ Home page")

def courses(request):
    return HttpResponse("This is first app/ courses page. ")

def about(request):
    return HttpResponse("This is first app/ about page. ")