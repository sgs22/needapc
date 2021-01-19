from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Choice, Response, QuizTakers


class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 4

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [ChoiceInline]
    extra = 10

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

class ResponseInline(admin.TabularInline):
    model = Response

class QuizTakersAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]

# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created')
#     fieldsets = [
#         (None,               {'fields': ['name']}),
#         (None,               {'fields': ['questions_count']}),
#         (None,               {'fields': ['description']}),
#     ]
#     inlines = [QuestionInline,]

# admin.site.register(Question, QuestionAdmin)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizTakers, QuizTakersAdmin)
admin.site.register(Response)