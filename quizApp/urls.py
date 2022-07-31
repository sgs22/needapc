from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
app_name = 'quizApp'
urlpatterns = [
    path('quizapp/<int:pk>/', views.QuestionDetail.as_view(), name='question_detail'),
    path('quizapp/questions/', views.QuestionList.as_view(), name='question_list'),
    path('quizapp/<slug:slug>/', views.QuizDetail.as_view(), name='quiz_detail'),
    path('quizapp/', views.QuizList.as_view(), name='quiz_list')
]
