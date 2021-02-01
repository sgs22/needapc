from . import views
from django.urls import path

"""
    Url paths extended from from django.urls
"""
app_name = 'questionary'
urlpatterns = [
    path('quest/', views.show_quests, name='quest'),
    path('response/', views.response_view, name='response')
]