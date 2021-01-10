from . import views
from django.urls import path

"""
    Url paths extended from from django.urls
"""
app_name = 'products'
urlpatterns = [
    path('products/', views.product_list_view, name='products'),
    path('products/<int:id>/', views.product_get_view),
]

    