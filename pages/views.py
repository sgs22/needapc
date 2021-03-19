from django.shortcuts import render

"""
    Current location
"""
def home_view(request, id=None, *args, **kwargs):
    return render(request, "index.html")

def about_view(request, *args, **kwargs):
    return render(request, "about.html")

def legal_view(request, *args, **kwargs):
    return render(request, "legal.html")