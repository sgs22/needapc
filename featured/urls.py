from . import views
from django.urls import path

urlpatterns = [
    path('featured/', views.featured_view, name='featured')
]

    