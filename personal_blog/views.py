from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    return render(request, 'personal_blog/home.html', {'posts': BlogPost.objects.all()})

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'personal_blog/post_detail.html', {'post': post})    

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content']
            )
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'personal_blog/create_post.html', {'form': form})