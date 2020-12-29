from . import views
from django.urls import path

"""
    Url paths extended from from django.urls
"""
urlpatterns = [
    path('featured/', views.featured_view, name='featured')
]

    