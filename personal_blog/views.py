from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    return render(request, 'personal_blog/home.html', {'posts': BlogPost.objects.all()})

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'personal_blog/post_detail.html', {'post': post})    