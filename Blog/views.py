from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blogsite,BlogPost
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def blog(request):
    blogs = Blogsite.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})
def team(request):
    return render(request, 'team.html')
def contact(request):
    return render(request, 'contact.html')
def courses(request):
    return render(request, 'courses.html')

# def myblogs(request):
#     blogs = Blogsite.objects.all()
#     template = loader.get_template('myblogs.html')
#     context = {
#         'blogs':blogs,
#     }
#     return HttpResponse(template.render( request,context))

def myblogs(request):
    blogs = Blogsite.objects.all()
    return render(request, 'myblogs.html',{'blogs':blogs})

def blog_user(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:list')  # Redirect to blog post list view
    else:
        form = BlogPost()
    return render(request, 'blog_user.html', {'form': form})
    
def user_blog_posts(request, username):
    user = User.objects.get(username=username)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'blog/user_blog_posts.html', {'user': user, 'posts': posts})


def list_blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/list_blog_posts.html', {'posts': posts})