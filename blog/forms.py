from .models import Comment
from django import forms

"""
    adds the fields to the form for comment on blog post
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')