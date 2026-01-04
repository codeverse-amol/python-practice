from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("allposts", views.blogpost),
    path("allposts/<slug:blog>", views.blog_post)
]