from django.db import models
from django.forms import ModelForm
from .models import Quiz, Question, Choice

'''
    TODO: update - Django form choices loaded from database are not updated
    https://www.codementor.io/tips/7714213398/django-form-choices-loaded-from-database-are-not-updated
'''
# class ChoiceForm(forms.ModelForm):
    # question_choices = forms.ModelChoiceField(choices=[])

    # def __init__(self, user, *args, **kwargs):
    #     super(ChoiceForm, self).__init__(*args, **kwargs)
    #     self.fields['choice_text'] = forms.ModelChoiceField(choices=[(choice.id, choice.choice_text) for choice in Choice.objects.all()])
    # class Meta:
    #     model = Choice
    #     fields = ['question', 'question_text']

