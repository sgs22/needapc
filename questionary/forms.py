from django.db import models
from django.forms import ModelForm
from .models import Questionary, Question, Choice, UserResponse

from django import forms

BUDGET_OPTIONS = ( 
    ("1", "250-300"), 
    ("2", "300-500"), 
    ("3", "500-750"), 
    ("4", "1000-1500"), 
    ("5", "1500+"), 
) 

USAGE_OPTIONS = ( 
    ("1", "Work"), 
    ("2", "School"), 
    ("3", "Leisure/Hobby"), 
    ("4", "Everything"), 
) 

WORKFLOW_OPTIONS = ( 
    ("1", "1-2 Apps"), 
    ("2", "2-4 Apps"), 
    ("3", "5+ Apps"), 
) 

APP_OPTIONS = ( 
    ("OFFICE", "Office Suite (Word etc)"), 
    ("ADOBE", "Adobe Suite i.e Photoshop etc."), 
    ("GAME_DEV", "Unity"), 
) 

class ResponseForm(ModelForm):
    class Meta:
        model = UserResponse
        fields = ('response_1','response_2','response_3','response_4',)
        exclude = ('user',)

    response_1 = forms.ChoiceField(choices=BUDGET_OPTIONS, widget=forms.RadioSelect(attrs={}))  #'class': 'form-check-inline'
    response_2 = forms.ChoiceField(choices=USAGE_OPTIONS, widget=forms.RadioSelect(attrs={}))
    response_3 = forms.ChoiceField(choices=WORKFLOW_OPTIONS, widget=forms.RadioSelect(attrs={}))
    response_4 = forms.MultipleChoiceField(choices = APP_OPTIONS) 

    

