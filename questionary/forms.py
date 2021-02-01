from django.db import models
from django.forms import ModelForm
from .models import Questionary, Question, Choice, UserResponse

from django import forms

class ResponseForm(ModelForm):
    class Meta:
        model = UserResponse
        fields = '__all__'
        exclude = ('user',)



