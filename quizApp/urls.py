from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
app_name = 'quizApp'
urlpatterns = [
    path('quizapp/<slug:slug>/<int:pk>/', views.question_detail, name='question_detail'),
    # path('quizapp/questions/', views.QuestionList.as_view(), name='question_list'),
    path('quizapp/<slug:slug>/', views.quiz_detail, name='quiz_detail'),
    path('quizapp/', views.QuizList.as_view(), name='quiz_list')
]
