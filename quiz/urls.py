from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
app_name = 'quiz'
urlpatterns = [
    path('quiz/', views.question_view, name='quiz'),
    path('quiz/<int:question_id>/', views.detail, name='detail'),
    path('quiz/<int:question_id>/results/', views.results, name='results'),
    path('quiz/<int:question_id>/vote/', views.vote, name='vote')
]
