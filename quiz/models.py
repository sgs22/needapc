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
class Quiz(models.Model):
    name = models.CharField(max_length=255, unique=True)
    questions_count = models.IntegerField(default=10)
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255, unique=True)
    description_text = models.TextField(max_length=500, unique=True)
    #question_image = models.ImageField(upload_to='quiz/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['created']  
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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
    
    def __str__(self):
        return self.choice_text

'''
    Model to store answers given by participant.
    NOTE: dont need questions here as they are only important for getting the answer
            and can be taken from the foreign key of the answer? 
'''
class QuizTakers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    selected_answers = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "QuizTaker"
        verbose_name_plural = "QuizTakers"
    
    def __str__(self):
        return self.user.username

    # def quiz_completed():
    #     if selected_answers != questions_count:
    #         completed = False



class Response(models.Model):
    quiztaker = models.ForeignKey(QuizTakers, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.question.question_text

'''
    make sure that the name of the quiz gets slugified and that the questions_count
     in the quiz is always equal to the number of questions related to that quiz
'''
@receiver(post_save, sender=Quiz)
def set_default_quiz(sender, instance, created,**kwargs):
    quiz = Quiz.objects.filter(id = instance.id)
    quiz.update(questions_count=instance.question_set.filter(quiz=instance.pk).count())

@receiver(post_save, sender=Question)
def set_default(sender, instance, created,**kwargs):
    quiz = Quiz.objects.filter(id = instance.quiz.id)
    quiz.update(questions_count=instance.quiz.question_set.filter(quiz=instance.quiz.pk).count())

@receiver(pre_save, sender=Quiz)
def slugify_title(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
