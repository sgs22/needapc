from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import ReviewForm

from .models import ProductDetail

'''
    TODO: Update product listing to use generic views?
'''
def product_list_view(request, id=None, *args, **kwargs):
    qs = ProductDetail.objects.all()
    return render(request, "products/products.html", {"product_list": qs})

def product_get_view(request, id=None, *args, **kwargs):
    template_name = "products/detail.html"
    try:
        product = ProductDetail.objects.get(id=id)
        reviews = product.reviews.filter(approved=True)
        new_review = None
    except ProductDetail.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.product = product
            new_review.user = request.user
            new_review.save()
    else:
        review_form = ReviewForm()
    return render(request, template_name, {"product": product,
                                           "reviews": reviews,
                                           "new_review": new_review,
                                           "review_form": review_form})



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

