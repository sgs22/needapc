from django import forms
from django.contrib.auth.models import User
from .models import QuizAnswer, Choice


class AnswerForm(forms.ModelForm):

    class Meta:
        model = QuizAnswer
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer_choice'].queryset = Choice.objects.filter(id=1)



  

