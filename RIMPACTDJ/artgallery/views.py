from django.shortcuts import render
from django.http import HttpResponse
from artgallery.models import Post, videoart, performances
# Create your views here.
def index(request):
    # Load all Images from DB
    posts = Post.objects.all()
    print(posts)
    data = {
        'posts': posts
    }
    return render(request, 'index.html', data)

def artgallery(request):
    posts = Post.objects.all()
    vidposts = videoart.objects.all()

   
    data = {
        'posts': posts,
        'vidposts': vidposts
    }

    print(vidposts)
    return render(request, 'artgall.html',data)

def post(request,url):
    post = Post.objects.get(title=url)
    print(post.title)
    return render(request,'post.html',{'post':post})


def techteam(request):
    return render(request,'techandm.html')

def performance(request):
    posts = performances.objects.all()
    perdata = {
        'perdata':posts
    }
    return render(request,'performances.html',perdata)