from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


from .models import FeaturedPost


"""
    Rendering template with query on all featured posts

    Filter by those that are marked published

    Order by newest featured products first
"""
def featured_view(request, id=None, *args, **kwargs):
    queryset = FeaturedPost.objects.filter(status=1).order_by('-created_on')
    return render(request, "featured/featured.html", {"featured_list": queryset})


# Rendering featured product in modal
# def featured_get_modal(request, id=None, *args, **kwargs):
#         try:
#         obj = FeaturedPost.objects.get(id=id)
#     except FeaturedPost.DoesNotExist:
#         raise Http404
#     return render(request, "products/detail.html", {"object":obj})