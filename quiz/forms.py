from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Quiz, Question, Choice, UserResponse

'''
    TODO: update - Django form choices loaded from database are not updated
    https://www.codementor.io/tips/7714213398/django-form-choices-loaded-from-database-are-not-updated
'''


class ResponseForm(ModelForm):
    class Meta:
        model = UserResponse
        fields = ('response_1','response_2',)
        exclude = ('quiztaker',)

    response_1 = forms.ModelChoiceField(queryset=Choice.objects.select_related('question').all(), widget=forms.RadioSelect(attrs={})) #THIS IS THE ANSWER!!! (RESPONSE 6 AND 7)
    response_2 = forms.ModelMultipleChoiceField(queryset=Choice.objects.all(), widget=forms.CheckboxSelectMultiple()) 

    #forms.ModelChoiceField(queryset=Choice.questions.all(), widget=forms.RadioSelect(attrs={}))

     #choice = forms.ChoiceField(choices=[(choice.pk, choice) for choice in MyChoices.objects.all()])
     #field2 = forms.ModelChoiceField(queryset=Articles.objects.all(), to_field_name="name")
    