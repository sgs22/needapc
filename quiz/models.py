import datetime
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
'''
    Not sure that more than one quiz is needed as only one quiz will be active on the site at a time
'''

TYPES = (
    (1, 'One answer'),
    (2, 'Multiple answer'),
    (3, 'Text answer'),
)

class Quiz(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, unique=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ['created']
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

class Question(models.Model):
    type = models.IntegerField(choices=TYPES, default=1, verbose_name='Question Type')
    question_number = models.PositiveIntegerField(blank=True, null=True)
    question_text = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, unique=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        ordering = ['question_number']  
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text


'''
    Django polls tutorial could be used here to record the number 
    of people selecting each choice for internal data insight?

    Could be updated to include linking to a user so that it can be saved
'''
class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz') #needed for fitlering forms 

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
    
    def __str__(self):
        return self.choice_text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE) quiz might need to be here...
    response_1 = models.CharField(max_length=200, null=True)
    response_2 = models.CharField(max_length=200, null=True)
    response_3 = models.CharField(max_length=200, null=True)

'''
    make sure that the name of the quiz gets slugified and that the questions_count
     in the quiz is always equal to the number of questions related to that quiz
'''
@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

