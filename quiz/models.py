from django.db import models

from django.contrib.auth.models import User

# class Quiz(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     questionCount = models.IntegerField(default=0)
#     description = models.CharField(max_length=70)
#     created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
#     updated_on = models.DateTimeField(auto_now= True)

#     class Meta:
#         verbose_name = "Quiz"
#         verbose_name_plural = "Quizzes"

class Question(models.Model):
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='quiz')
    question_text = models.CharField(max_length=200, unique=True)
    description_text = models.CharField(max_length=50, unique=True)
    question_image = models.ImageField(upload_to='quiz/%Y/%m/%d/', max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    # user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_quiz', default=0)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
    
    # def __str__(self):
    #     return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # progress = models.IntegerField("progress")
    # user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_results', default=0)

    # def __str__(self):
    #     return self.answer

