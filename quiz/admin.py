from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Choice, UserResponse


class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 0

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [ChoiceInline]
    extra = 0

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

class ResponseInline(admin.TabularInline):
    model = UserResponse
    extra = 0


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
admin.site.register(UserResponse)