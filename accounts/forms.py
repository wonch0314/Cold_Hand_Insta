from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):

    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control mb-4'
            }
        )
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                    'class': 'form-control mb-4',
                    }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password',
                    'class': 'form-control mb-4',
                    }))


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'image_url',)
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control mb-4'
            }
        )
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    
    class Meta(PasswordChangeForm):
        model = User
        fields = ('__all__')