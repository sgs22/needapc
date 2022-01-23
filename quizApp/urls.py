from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
app_name = 'quizApp'
urlpatterns = [
    path('quizapp/', views.get_answer(), name='quiz_list'),
]
