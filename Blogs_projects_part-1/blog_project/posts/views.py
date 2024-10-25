from django.shortcuts import render, redirect
from . import forms
from . import models


# Create your views here.
def add_Post(request):
    if request.method == 'POST':
        post_form = forms.PostFrom(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_Post')
    else:
        post_form = forms.PostFrom()
    return render(request, 'add_post.html', {'form' : post_form})

def edit_Post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostFrom(instance=post)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.PostFrom(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
        
    return render(request, 'add_post.html', {'form' : post_form})

def delete_Post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')