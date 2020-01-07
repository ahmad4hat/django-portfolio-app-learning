from django.shortcuts import render
from . import models

# Create your views here.


def allBlogs(request):
    blogs = models.Blog.objects
    return render(request, "blog/allblogs.html", {"blogs": blogs})
