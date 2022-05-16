from multiprocessing import AuthenticationError
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomPasswordChangeForm, UserForm, CustomUserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import User
from feeds.models import Feed, Comment

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feeds:index')
    else:
        form = UserForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)

def login(request):

    if request.user.is_authenticated:
        return redirect('feeds:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)

            next_url = request.GET.get('next')
            return redirect(next_url or 'feeds:index')
    
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('feeds:index')

def profile(request,username):
    user = User.objects.get(username=username)
    feeds = user.user_feeds.all()
    comments = user.user_comments.all()
    context = {
        'user':user,
        'feeds': feeds,
        'comments': comments,
    }
    return render(request,'accounts/profile.html',context)

def follows(request,username):
    you  = get_object_or_404(get_user_model(),username=username)
    me = request.user

    if you.username != me.username:
        if you.followers.filter(username=me.username).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    
    return redirect('accounts:profile',you.username)

def update(request, username):
    you  = get_object_or_404(get_user_model(),username=username)
    me = request.user
    if you.username == me.username:
        if request.method == 'GET':
            form = CustomUserChangeForm(instance = you)
            context = {
                'form': form
            }
            return render(request, 'accounts/update.html', context)
        elif request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=you)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile', you.username)
            context = {
                'form': form
            }
            return render(request, 'accounts/update.html', context)
    return redirect('accounts:profile', username)

def password(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile', user.username)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html', {'form': form})