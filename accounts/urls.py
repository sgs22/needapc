from django.urls import path
from .views import  accounts, SignUpView, validate_username

"""
    Url paths extended from from django.urls
"""
urlpatterns = [
    path('accounts/', accounts, name='accounts'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/validate_username/', validate_username, name='validate_username')
]