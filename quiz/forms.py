from .models import QuizAnswer
from django import forms

class QuizForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ('answer', 'progress')