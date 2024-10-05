from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        moel = Comment
        fields = ["user_name", "user_email", "message"]