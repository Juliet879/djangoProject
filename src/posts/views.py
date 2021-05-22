from typing import ContextManager
from django.http import request
from django.shortcuts import render
from .models import Post

# Create your views here.

# CRUD - Create Retrieve Update Delete

# Create lists of the posts

def posts_list_view(request):
    book_post = Post.objects.all()
    context = {
       'book_post': book_post
    }
    return render(request,"posts/index.html",context)

