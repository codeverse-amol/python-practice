from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("allposts", views.blogpost, name="all-posts"),
    path("allposts/<slug:blog>", views.blog_post, name="blog_post")
]