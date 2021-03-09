from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Quiz, Question, Choice, UserResponse, Application

'''
    TODO: update - Django form choices loaded from database are not updated
    https://www.codementor.io/tips/7714213398/django-form-choices-loaded-from-database-are-not-updated

    TODO: When adding more than one quiz, you get duplicate choices if they have the same question number

    NOTES: Queries for Foreign key object lookup:
    https://docs.djangoproject.com/en/dev/topics/db/queries/#lookups-that-span-relationships
    https://www.agiliq.com/blog/2014/04/django-backward-relationship-lookup/

    TODO: ADD additional forms for other quizzes i.e. one for Laptop one for Desktop.

'''
# question_instance = Question.objects.filter(question_number=1)
# question_name = question_instance.values('question_text')

class ResponseForm(ModelForm):
    class Meta:
        model = UserResponse
        fields = ('response_1','response_2','response_3','response_4',)
        exclude = ('user',)

    response_1 = forms.ModelChoiceField(label=Question.objects.get(question_number=1,quiz__title="Laptop"),
                                        queryset=Choice.objects.filter(question__question_number=1,quiz__title="Laptop"),
                                        widget=forms.RadioSelect(attrs={}))
    response_2 = forms.ModelMultipleChoiceField(label=Question.objects.get(question_number=2,quiz__title="Laptop"),
                                        queryset=Choice.objects.filter(question__question_number=2,quiz__title="Laptop"),
                                        widget=forms.CheckboxSelectMultiple()) 
    response_3 = forms.ModelChoiceField(label=Question.objects.get(question_number=3,quiz__title="Laptop"),
                                        queryset=Choice.objects.filter(question__question_number=3,quiz__title="Laptop"), 
                                        widget=forms.RadioSelect(attrs={}))
    response_4 = forms.ModelMultipleChoiceField(label=Question.objects.get(question_number=4,quiz__title="Laptop"),
                                        queryset=Application.objects.filter(active=True),
                                        widget=forms.CheckboxSelectMultiple()) 
                                        










    #forms.ModelChoiceField(queryset=Choice.questions.all(), widget=forms.RadioSelect(attrs={}))

    #choice = forms.ChoiceField(choices=[(choice.pk, choice) for choice in MyChoices.objects.all()])
    #field2 = forms.ModelChoiceField(queryset=Articles.objects.all(), to_field_name="name")
    
    #Choice.objects.filter(question__question_number=1)
    #response_1 = forms.ModelChoiceField(queryset=Choice.objects.select_related('question').all(), widget=forms.RadioSelect(attrs={})) #OLD LOOK UP METHOD