from django.urls import path
from . import views

"""
    Url paths extended from from django.urls
"""
app_name = 'quiz'
urlpatterns = [
    path('quiz/', views.QuizList.as_view(), name='quiz_list'),
    path("quiz/<slug:slug>/", views.quiz_detail, name="quiz_detail"),
    path("quiz/<slug:slug>/overview/", views.overview_view, name="overview_view"),
    path("quiz/<slug:slug>/results/", views.results_view, name="results_view")
    #add - results of each questionnaire url
]

    #path('quiz/', views.response_view, name='response')
    #path('quiz/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('quiz/<int:question_id>/vote/', views.vote, name='vote'),
    #path('quiz/<int:pk>/', views.DetailView.as_view(), name='detail'),