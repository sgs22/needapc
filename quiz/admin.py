from django.contrib import admin

from .models import QuizQuestion

# Register your models here.
# class QuizQuestion(admin.ModelAdmin):

admin.site.register(QuizQuestion)