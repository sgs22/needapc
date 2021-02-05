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
        fields = ('response_1','response_2','response_3','response_4','response_5','response_6','response_7',)
        exclude = ('user',)

    response_1 = forms.ChoiceField(choices=BUDGET_OPTIONS, widget=forms.RadioSelect(attrs={}))  #'class': 'form-check-inline'
    response_2 = forms.ChoiceField(choices=USAGE_OPTIONS, widget=forms.RadioSelect(attrs={}))
    response_3 = forms.ChoiceField(choices=WORKFLOW_OPTIONS, widget=forms.RadioSelect(attrs={}))
    response_4 = forms.MultipleChoiceField(choices = APP_OPTIONS, widget=forms.CheckboxSelectMultiple()) 
    response_5 = forms.ChoiceField(choices=[(choice.pk, choice) for choice in Choice.objects.all()])
    response_6 = forms.ModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect(attrs={})) #THIS IS THE ANSWER!!! (RESPONSE 6 AND 7)
    response_7 = forms.ModelMultipleChoiceField(queryset=Choice.objects.all(), widget=forms.CheckboxSelectMultiple()) 

    #forms.ModelChoiceField(queryset=Choice.questions.all(), widget=forms.RadioSelect(attrs={}))

     #choice = forms.ChoiceField(choices=[(choice.pk, choice) for choice in MyChoices.objects.all()])
     #field2 = forms.ModelChoiceField(queryset=Articles.objects.all(), to_field_name="name")