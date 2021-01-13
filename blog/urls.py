from . import views
from django.urls import path

"""
    Url paths extended from from django.urls
    BUG: enabling app_name causes a django.urls.exceptions.NoReverseMatch error 500.
"""
# app_name = 'blog' 
urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path("blog/<slug:slug>/", views.post_detail, name="post_detail")
]