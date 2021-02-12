from django.urls import path
from .views import  accounts, SignUpView, validate_username, validate_email, change_password

"""
    Url paths extended from from django.urls
"""
app_name = 'accounts'
urlpatterns = [
    path('accounts/', accounts, name='accounts'),
    path('accounts/change_password/', change_password, name='change_password'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/validate_username/', validate_username, name='validate_username'),
    path('accounts/validate_email/', validate_email, name='validate_email')
]