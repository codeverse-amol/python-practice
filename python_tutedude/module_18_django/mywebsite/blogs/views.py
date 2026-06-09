from datetime import date
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

blog_details = [
    {
        "slug": "python_intro",
        "image": "python.png",
        "date": date(2025, 10, 15),
        "title": "Python Introduction",
        "preview": """Python is an open-source, high-level programming language known for its
        simplicity and readability. It is widely used in web development, data science,
        automation, AI, and machine learning.""",
        "content": """Python is one of the most popular programming languages in the world due to its clean syntax and beginner-friendly nature. It allows developers to write fewer lines of code while accomplishing complex tasks. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming, making it highly versatile.

    Python is extensively used in various domains such as web development, data analysis, artificial intelligence, machine learning, automation, and scientific computing. Frameworks like Django and Flask simplify web application development, while libraries such as NumPy, Pandas, and TensorFlow power data-driven applications. Because of its large community and rich ecosystem, Python continues to be a top choice for both beginners and experienced developers."""
    }
,
    {
        "slug": "django_basic",
        "image": "django.png",
        "date": date(2025, 10, 20),
        "title": "Django Basics",
        "preview": """Django is a high-level Python web framework that enables rapid development
        of secure and scalable web applications using a clean and pragmatic design.""",
        "content": """Django is a powerful and widely used web framework built on top of Python. It follows the Model-View-Template (MVT) architecture, which helps developers structure applications in a clean and maintainable way. Django comes with many built-in features such as authentication, admin interface, ORM (Object Relational Mapper), and security protections, allowing developers to focus more on business logic rather than repetitive tasks. One of the biggest advantages of Django is its “batteries-included” philosophy. This means that Django provides most of the tools required to build a complete web application out of the box. From handling URL routing to managing databases and rendering templates, Django simplifies the entire development process. Because of its scalability and robustness, Django is used by many large platforms and startups alike to build reliable web applications quickly."""
    }
,
    {
        "slug": "python_oops",
        "image": "python_oops.png",
        "date": date(2025, 10, 25),
        "title": "Object-Oriented Programming in Python",
        "preview": """Object-Oriented Programming (OOP) in Python is a programming paradigm
        that organizes code into reusable objects and classes, improving structure and maintainability.""",
        "content": """Object-Oriented Programming (OOP) is a core concept in Python that helps developers design programs using classes and objects. A class acts as a blueprint for creating objects, while objects are instances of classes that contain data (attributes) and behavior (methods). Python supports OOP principles such as encapsulation, inheritance, polymorphism, and abstraction, making it suitable for building complex and scalable applications.

    Encapsulation allows data to be protected and accessed through methods, improving security and data integrity. Inheritance enables one class to derive properties and methods from another, reducing code duplication. Polymorphism allows methods to behave differently based on the object calling them, while abstraction focuses on exposing only essential features. By using OOP in Python, developers can write cleaner, modular, and more maintainable code, which is especially useful in large projects and frameworks like Django."""
    }
,
    {
        "slug": "regex",
        "image": "regex.jpg",
        "date": date(2025, 10, 30),
        "title": "Regular Expressions in Python",
        "preview": """Regular Expressions (Regex) are powerful patterns used to search, match,
        and manipulate strings efficiently in Python.""",
        "content": """Regular Expressions, commonly known as Regex, are used in Python to perform complex pattern matching and text processing tasks. The `re` module in Python provides functions such as `search`, `match`, `findall`, and `sub` that allow developers to work with strings more effectively. Regex is widely used in tasks like data validation, log analysis, web scraping, and text transformation.

    Using regex, developers can define patterns to match email addresses, phone numbers, passwords, or specific text formats. Although regex syntax may look complex at first, mastering it can greatly reduce the amount of code needed to process strings. In Python applications, regex plays a crucial role in handling user input validation and data extraction, making it an essential skill for any Python developer."""
    }

]


def home(request):
    sorted_blogs = sorted(blog_details, key=lambda post:post['date'], reverse=True)
    latest_blogs = sorted_blogs[:2]
    return render(request, "blogs/index.html", {"l_blogs": latest_blogs})
    # res_data = render_to_string("blogs/index.html")
    # return HttpResponse(res_data)


def blogpost(request):
    return render(request, "blogs/blogpost.html", {"blogs": blog_details})
    # for b in blog_list:
    #     blog_path = reverse("blog_post", args=[b])
    #     list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'

    # res_data = f"<u1>{list_items}</u1>"

    # res_data = """
    # <u1>
    #     <li><a href="allposts/python_intro">Python Intro</a></li>
    #     <li><a href="allposts/django_basic">Django Basic</a></li>
    #     <li><a href="allposts/python_oops">Python OOPs</a></li>
    #     <li><a href="allposts/regex">Regex</a></li>
    # </u1> 
    #     """
    # return HttpResponse(res_data)


def process_blog_name(blog):
    # "python-intro" => ["python", "intro"] ==> "python intro" => "Python Intro"
    blog_list = blog.split("_")
    return " ".join(blog_list)



# def python_intro(request):
#     return HttpResponse("<h1>Python post</h1>")

# def django_basic(request):
#     return HttpResponse("<h1>Django basics blog posts</h1>")

# def python_oops(request):
#     return HttpResponse("<h1>Object-oriented programming with python</h1>")


def get_blog_by_slug(blog_url):
    for blog in blog_details:
        if blog['slug'] == blog_url:
            return blog
        

def blog_post(request, blog):
    try:
        res = get_blog_by_slug(blog)
        return render(request, "blogs/posts.html", {"post": res})
    except Exception:
        raise Http404()
      

# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)
