from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    student = models.MyModel.objects.all()
    return render(request, "home.html", {'data' : student})

def delete_student(request, roll):
    std = models.MyModel.objects.get(pk = roll).delete()
    return redirect("homepage")