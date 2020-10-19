from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


from .models import ProductDetail

def home_view(request, id=None, *args, **kwargs):
    return render(request, "base.html")

def product_list_view(request, id=None, *args, **kwargs):
    qs = ProductDetail.objects.all()
    return render(request, "products/products.html", {"object_list:": qs})