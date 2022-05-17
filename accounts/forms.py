from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserForm(UserCreationForm):

    
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
        fields = ('old_password', 'new_password1', 'new_password2')
    
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Old Password',
                    'class': 'form-control mb-4',
                }))
    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'New Password',
                    'class': 'form-control mb-4',
                    }))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm New Password',
                    'class': 'form-control mb-4',
                    }))


class CustomAuthenticationForm(AuthenticationForm):
    
    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )
    
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )