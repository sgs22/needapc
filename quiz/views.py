from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# Create your views here.

def quiz_view(request, id=None, *args, **kwargs):
    return render(request, "quiz/quiz.html")