from . import views
from django.urls import path

# urlpatterns = [
#     path('blog/', views.PostList.as_view(), name='blog'),
#     path("blog/<slug:slug>/", views.post_detail, name="post_detail"),
# ]

urlpatterns = [
    path('products/', views.product_list_view, name='products'),
    path('products/<int:id>/', views.product_get_view),
]

    