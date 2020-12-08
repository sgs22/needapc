from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=50, unique=True)
    questionCount = models.IntegerField(default=0)
    description = models.CharField(max_length=70)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

# class QuizQuestion(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='comments')
#     title = models.CharField(max_length=50, unique=True)
#     subTitle = models.CharField(max_length=50, unique=True)
#     image = models.ImageField(upload_to='quiz/%Y/%m/%d/', max_length=255, null=True, blank=True)
#     option1 = models.CharField(max_length=50, unique=True)
#     option2 = models.CharField(max_length=50, unique=True)
#     option3 = models.CharField(max_length=50, unique=True)
#     option4 = models.CharField(max_length=50, unique=True)
#     user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_quiz')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
    
    def __str__(self):
        return self.title

# class QuizAnswer(models.Model):
#     question = models.ForeignKey(QuizQuestion,on_delete=models.CASCADE, related_name='questions')
#     answer = models.CharField(max_length=50)
#     progress = models.IntegerField("progress")
#     user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_results')

#     class Meta:
#         verbose_name = "Answer"
#         verbose_name_plural = "Answers"

#     def __str__(self):
#         return self.answer

