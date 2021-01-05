from django.urls import path
from .views import  accounts, SignUpView, validate_username, validate_email

"""
    Url paths extended from from django.urls
"""
urlpatterns = [
    path('accounts/', accounts, name='accounts'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/validate_username/', validate_username, name='validate_username'),
    path('accounts/validate_email/', validate_email, name='validate_email')
]