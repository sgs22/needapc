from django.shortcuts import render
from .models import Choice, Question, Questionary, UserResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .forms import ResponseForm

def show_quests(request):
    quests = Questionary.objects.all()
    quest = quests.first() # Select the first quiz
    context = { 'quest': quest }
    #t = loader.get_template('questionary/quest.html')
    return render(request, 'questionary/quest.html', {'quest': quest })


@login_required
def response_view(request):
    form = ResponseForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = request.user
        response.save()
    
    context = {'form' : form }
    return render(request, "questionary/response.html", context)

