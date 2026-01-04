from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def home(request):
    return HttpResponse("Home page of our Blogs")


def blogpost(request):
    return HttpResponse("All blog posts")

def python_intro(request):
    return HttpResponse("Python post")

def django_basic(request):
    return HttpResponse("Django basics blog posts")

def python_oops(request):
    return HttpResponse("Object-oriented programming with python")

def blog_post(request, blog):
    if blog == "python_intro":
        res = "Python post"
    elif blog == "django_basic":
        res = "Django basics blog posts"
    elif blog == "python_oops":
        res = "Object-oriented programming with python"
    else:
        return HttpResponseNotFound("Blog not found")
    return HttpResponse(res)


# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)
