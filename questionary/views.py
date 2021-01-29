from django.shortcuts import render
from .models import Choice, Question, Questionary
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import loader

def show_quests(request):
    quests = Questionary.objects.all()
    quest = quests.first() # Select the first quiz
    context = { 'quest': quest }
    #t = loader.get_template('questionary/quest.html')
    return render(request, 'questionary/quest.html', {'quest': quest })


# def choose(request):
