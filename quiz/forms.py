from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Quiz, Question, Choice

'''
    TODO: update - Django form choices loaded from database are not updated
    https://www.codementor.io/tips/7714213398/django-form-choices-loaded-from-database-are-not-updated
'''


class MyForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    