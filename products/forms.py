from .models import Review
from django import forms

"""
    adds the fields to the form for comment on blog post
"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'title', 'body')