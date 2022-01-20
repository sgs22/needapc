from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")

    class Meta:
        ordering = ['created']
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=255, unique=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        ordering = ['question_number']  
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions', related_query_name='question')

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
    
    def __str__(self):
        return self.choice_text

class QuizAnswer(models.Model):
    answer_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='choices', related_query_name='choice')
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"