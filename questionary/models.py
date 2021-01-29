from django.db import models
from django.contrib.auth.models import User

class Choice(models.Model):
    choice_text = models.CharField(max_length=255)

class Question(models.Model):
    question_text = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, unique=False)
    choices = models.ManyToManyField(Choice, null=True)

class Questionary(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, unique=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()
    active = models.BooleanField(default=True, db_index=True)
    questions = models.ManyToManyField(Question, null=True)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user associated with answering
    response = models.ManyToManyField(Choice) # the choices they selected
    response_date = models.DateTimeField(blank=True, null=True) # the datetime when they did the quiz