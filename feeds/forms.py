from django import forms
from .models import Feed, Comment

class FeedForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ('content','image_url')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)