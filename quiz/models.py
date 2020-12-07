from django.db import models
from django.contrib.auth.models import User

class QuizQuestion(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subTitle = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='quiz/%Y/%m/%d/', max_length=255, null=True, blank=True)
    option1 = models.CharField(max_length=50, unique=True)
    option2 = models.CharField(max_length=50, unique=True)
    option3 = models.CharField(max_length=50, unique=True)
    option4 = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title

class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion,on_delete=models.CASCADE, related_name='questions')
    answer = models.CharField(max_length=50)
    progress = models.IntegerField("progress")

    def __str__(self):
        return self.answer