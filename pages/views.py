from django.shortcuts import render

from .models import IndexPost

"""
    Current location
"""
# def home_view(request, id=None, *args, **kwargs):
#     return render(request, "index.html")

def home_view(request, id=None, *args, **kwargs):
    queryset = IndexPost.objects.filter(status=1).order_by('-created_on')
    return render(request, "index.html", {"index_list": queryset})

def about_view(request, *args, **kwargs):
    return render(request, "about.html")

def legal_view(request, *args, **kwargs):
    return render(request, "legal.html")