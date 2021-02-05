from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
    TODO: add slug of quiz after initial url so that more than one quiz can be added.
"""
app_name = 'quiz'
urlpatterns = [
    path('quiz/', views.QuizView.as_view(), name='quiz'),
    path('quiz/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('quiz/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('quiz/<int:question_id>/vote/', views.vote, name='vote'),
    path('quiz/response/', views.response_view, name='response')
]
