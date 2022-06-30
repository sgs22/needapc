from django import forms
from django.contrib.auth.models import User
from .models import QuizAnswer, Choice


class AnswerForm(forms.ModelForm):

    class Meta:
        model = QuizAnswer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer_choice'].queryset = Choice.objects.filter(id=1)
        self.fields['user'].queryset = User.objects.filter(id=1)



    # init method to filter out choices for each modelform for each question request.user

