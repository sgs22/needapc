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
from django.urls import path

from django.conf import settings
from django.views.static import serve

from products.views import (
    product_create_view,
    product_list_view,
    product_get_view,
    home_view,
    base_view,
)

urlpatterns = [
    path('', home_view),
    path('products/', product_list_view),
    path('products/<int:id>/', product_get_view),
    path('base/', base_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
