"""needapc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from pages.views import home_view, about_view, legal_view

from products.views import (
    product_list_view,
    product_get_view,
)

from featured.views import (
    featured_view
)

from accounts.views import (
    login_view, 
    logout_view,
    register_view
)

urlpatterns = [
    path('', home_view),
    path('', include('quiz.urls', namespace="quiz")),
    path('', include('featured.urls', namespace="featured")),
    path('', include('accounts.urls', namespace="accounts")),
    path('', include('products.urls', namespace="products")),
    path('', include('blog.urls', namespace="blog")),
    path('accounts/', include('allauth.urls')),
    path('about/', about_view, name='about'),
    path('legal/', legal_view, name='legal'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

