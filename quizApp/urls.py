from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
app_name = 'quizApp'
urlpatterns = [
    path('quizApp/<slug:slug>/', views.QuizDetail.as_view(), name='quiz_detail'),
    path('quizapp/', views.QuizList.as_view(), name='quiz_list')
]
