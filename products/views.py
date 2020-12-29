from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


from .models import ProductDetail

"""
    Current location
"""
def home_view(request, id=None, *args, **kwargs):
    return render(request, "index.html")

def product_list_view(request, id=None, *args, **kwargs):
    qs = ProductDetail.objects.all()
    return render(request, "products/products.html", {"object_list": qs})

def product_get_view(request, id=None, *args, **kwargs):
    try:
        obj = ProductDetail.objects.get(id=id)
    except ProductDetail.DoesNotExist:
        raise Http404
    return render(request, "products/detail.html", {"object":obj})

# # currently using admin to import new products but could be useful in future
# def product_create_view(request, id=None, *args, **kwargs):
#     context = {}
#     form = ProductDetailForm(request.POST or None)
#     context["form"] = form
#     if form.is_valid():
#         form.save()
#         form = ProductDetailForm()
#         context["added"] = True
#         context["form"] = form

#     return render(request, "base.html", context)

# def base_view(request, id=None, *args, **kwargs):
#     return render(request, "base.html")