from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

blog_names = {
    "python_intro":"Introduction to Python",
    "django_basic":"Django basics blog posts",
    "python_oops":"Object-oriented programming with python",
    "regex":"Regular expression in python"
}

def home(request):
    return render(request, "blogs/index.html")
    # res_data = render_to_string("blogs/index.html")
    # return HttpResponse(res_data)


def blogpost(request):
    list_items = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog_post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'

    res_data = f"<u1>{list_items}</u1>"

    # res_data = """
    # <u1>
    #     <li><a href="allposts/python_intro">Python Intro</a></li>
    #     <li><a href="allposts/django_basic">Django Basic</a></li>
    #     <li><a href="allposts/python_oops">Python OOPs</a></li>
    #     <li><a href="allposts/regex">Regex</a></li>
    # </u1> 
    #     """
    return HttpResponse(res_data)


def process_blog_name(blog):
    # "python-intro" => ["python", "intro"] ==> "python intro" => "Python Intro"
    blog_list = blog.split("_")
    return " ".join(blog_list).title()



# def python_intro(request):
#     return HttpResponse("<h1>Python post</h1>")

# def django_basic(request):
#     return HttpResponse("<h1>Django basics blog posts</h1>")

# def python_oops(request):
#     return HttpResponse("<h1>Object-oriented programming with python</h1>")

def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {"blog_text":res, "blog_name":process_blog_name(blog)})
    except Exception:
        return HttpResponseNotFound("<h1>Blog not found</h1>")
    else:
        return HttpResponse(res)


# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)
