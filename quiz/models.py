from django.db import models

from django.contrib.auth.models import User
'''
    Not sure that more than one quiz is needed as only one quiz will be active on the site at a time
'''

class Question(models.Model):
    question_text = models.CharField(max_length=120, unique=True)
    description_text = models.TextField(max_length=250, unique=True)
    question_image = models.ImageField(upload_to='quiz/%Y/%m/%d/', max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


'''
    Django polls tutorial could be used here to record the number 
    of people selecting each choice for internal data insight?

    Could be updated to include linking to a user so that it can be saved
'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"



