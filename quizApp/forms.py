from django import forms
from django.contrib.auth.models import User
from .models import QuizAnswer, Choice, Question


class AnswerForm(forms.ModelForm):

    class Meta:
        model = QuizAnswer
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', None)
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer_choice'] = forms.ModelChoiceField(
            required=True,
            queryset=choices,
            widget=forms.RadioSelect
        )
