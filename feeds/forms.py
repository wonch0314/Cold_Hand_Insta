from django import forms
from .models import Feed, Comment

class FeedForm(forms.ModelForm):
    
    class Meta:
        model = Feed
        fields = ('content','image_url')
    
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control p-4'
            }
        )
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)