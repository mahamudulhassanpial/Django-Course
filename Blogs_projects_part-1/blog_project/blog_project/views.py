from django.shortcuts import render
from posts.models import Post

def home(request):
    data = Post.objects.all()
    print(data)
    # for i in data:
    #     print(i.title, i.catagory)
    return render(request, 'home.html', {'data' : data})