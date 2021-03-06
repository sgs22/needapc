from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Quiz, Question, Choice, UserResponse, Application

'''
    TODO: update - Django form choices loaded from database are not updated
    https://www.codementor.io/tips/7714213398/django-form-choices-loaded-from-database-are-not-updated

    TODO: When adding more than one quiz, you get duplicate choices if they have the same question number

    NOTES: Queries for Foreign key object lookup:
    https://docs.djangoproject.com/en/dev/topics/db/queries/#lookups-that-span-relationships
    https://www.agiliq.com/blog/2014/04/django-backward-relationship-lookup/

    TODO: ADD additional forms for other quizzes i.e. one for Laptop one for Desktop.
    
    #TODO: ADD IF STATEMENT VAILDATION FOR IF QUIZ IS FOUND THEN DISPLAY ELSE SHOW ERROR SO THAT THE WEB APP RUNS!

'''
# question_instance = Question.objects.filter(question_number=1)
# question_name = question_instance.values('question_text')

class ResponseForm(ModelForm):
    class Meta:
        model = UserResponse
        fields = ('__all__')
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        for question in Question.objects.all():
            if question.type==1:
                self.fields['response_1'] = forms.ModelChoiceField(label=Question.objects.get(question_number=1,quiz__title="Laptop"),         #response for budget
                                        queryset=Choice.objects.filter(question__question_number=1,quiz__title="Laptop"),
                                        widget=forms.RadioSelect())
            

    response_1 = forms.ModelChoiceField(label=Question.objects.get(question_number=1,quiz__title="Laptop"),         #response for budget
                                        queryset=Choice.objects.filter(question__question_number=1,quiz__title="Laptop"),
                                        widget=forms.RadioSelect())
    response_2 = forms.ModelMultipleChoiceField(label=Question.objects.get(question_number=2,quiz__title="Laptop"), #response for workflow
                                        queryset=Choice.objects.filter(question__question_number=2,quiz__title="Laptop"),
                                        widget=forms.CheckboxSelectMultiple()) 
    response_3 = forms.ModelChoiceField(label=Question.objects.get(question_number=3,quiz__title="Laptop"),         #response for 
                                        queryset=Choice.objects.select_related('question'), 
                                        widget=forms.RadioSelect())
    response_4 = forms.ModelMultipleChoiceField(label=Question.objects.get(question_number=4,quiz__title="Laptop"), #response for app selection
                                        queryset=Application.objects.filter(active=True),
                                        widget=forms.CheckboxSelectMultiple()) 

                                        
    # gets form widget based on type of question, 1 = one answer, 2 = Multiple, 3 = Text answer
    def getQuestionType(*args, **kwargs):
        if Question.objects.get(type=1):
            questionType = RadioSelect()
        elif Question.objects.get(type=2):
            questionType = CheckboxSelectMultiple()
        else:
            questionType = TextInput()









    #forms.ModelChoiceField(queryset=Choice.questions.all(), widget=forms.RadioSelect(attrs={}))

    #choice = forms.ChoiceField(choices=[(choice.pk, choice) for choice in MyChoices.objects.all()])
    #field2 = forms.ModelChoiceField(queryset=Articles.objects.all(), to_field_name="name")
    
    #Choice.objects.filter(question__question_number=1)
    #response_1 = forms.ModelChoiceField(queryset=Choice.objects.select_related('question').all(), widget=forms.RadioSelect(attrs={})) #OLD LOOK UP METHOD