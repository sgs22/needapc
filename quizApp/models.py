from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.urls import reverse


class Quiz(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=200, unique=True, default="test")

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quizApp:quiz_detail', kwargs={'slug': self.slug})

    def get_questions(Self):
         return self.question_set.all()


class Question(models.Model):
    question_order = models.IntegerField(blank=False, default=1)
    question_text = models.CharField(max_length=255, unique=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def get_absolute_url(self):
        return reverse('quizApp:question_detail', kwargs={'slug':self.quiz.slug, 'pk': self.pk})

    def __str__(self):
        return self.question_text

    def get_choices(self):
        return self.question_choices.all()


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        return f"Question: {self.question.question_text}, Choice: {self.choice_text}"


class QuizAnswer(models.Model):
    answer_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


'''
    make sure that the name of the quiz gets slugified and that the questions_count
     in the quiz is always equal to the number of questions related to that quiz
'''


@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
