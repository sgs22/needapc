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
        ordering = ['pub_date'] 
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
    choice_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
    
    def __str__(self):
        return self.choice_text

# class QuizAnswer(models.Model):
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default=DEFAULT_CHOICE_ID)
#     user_answer = models.CharField(max_length=120)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = "QuizAnswer"
#         verbose_name_plural = "QuizAnswers"
    
    # def __str__(self):
    #     return self.user_answer



