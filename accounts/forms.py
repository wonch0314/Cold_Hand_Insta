from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)