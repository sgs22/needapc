from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
urlpatterns = [
    path('quiz/', views.question_view, name='q_view'),
    path('quiz/<int:question_id>/', views.detail, name='detail')
]
