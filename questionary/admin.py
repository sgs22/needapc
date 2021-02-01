from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Questionary, UserResponse

# class FeaturedAdmin(admin.Modeladmin):

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Questionary)
admin.site.register(UserResponse)