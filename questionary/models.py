from django.db import models
from django.contrib.auth.models import User

#TODO: ratehr than manually assigning options in model
#    - initilaise the form with choices made for each question

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
class Choice(models.Model):
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text

class Question(models.Model):
    question_text = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, unique=False)
    choices = models.ManyToManyField(Choice)

class Questionary(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, unique=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()
    active = models.BooleanField(default=True, db_index=True)
    questions = models.ManyToManyField(Question)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    response_1 = models.CharField(max_length=20,choices=BUDGET_OPTIONS)
    response_2 = models.CharField(max_length=20,choices=USAGE_OPTIONS)
    response_3 = models.CharField(max_length=20,choices=WORKFLOW_OPTIONS)
    response_4 = models.CharField(max_length=200, null=True)
    response_5 = models.CharField(max_length=200, null = True)
    response_6 = models.CharField(max_length=200, null=True)
    response_7 = models.CharField(max_length=200, null=True)

    # def __str__(self):
    #     return self.id
    
