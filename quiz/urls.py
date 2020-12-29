from django.urls import path
from .views import choice_view

"""
    Url paths extended from from django.urls
"""
urlpatterns = [
    path('quiz/', choice_view, name='choice_view'),
    # path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # path('accounts/validate_username/', validate_username, name='validate_username')
]

    # path('quiz/', quiz_view),