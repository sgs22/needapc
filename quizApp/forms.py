from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import QuizAnswer, Choice, Question


class AnswerForm(forms.ModelForm):

    class Meta:
        model = QuizAnswer
        exclude = ["user"]
        widgets = {
            'answer_choice': forms.RadioSelect
        }

    def __init__(self, question, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer_choice'] = forms.ChoiceField(
            choices=[(o.id, str(o)) for o in Choice.objects.filter(id=question)]
        )


  

