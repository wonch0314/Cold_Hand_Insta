from multiprocessing import AuthenticationError
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from pkg_resources import require
from .forms import CustomPasswordChangeForm, CustomUserForm, CustomUserChangeForm, CustomAuthenticationForm

from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .models import User


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feeds:index')
    else:
        form = CustomUserForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)

@login_required
@require_POST
def delete(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == "POST":
        if request.user == user:
            user.delete()
        return redirect('feeds:index')
        
            
        
        

def login(request):

    if request.user.is_authenticated:
        return redirect('feeds:index')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)

            next_url = request.GET.get('next')
            return redirect(next_url or 'feeds:index')
    
    else:
        form = CustomAuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('feeds:index')

@login_required
def js_follows(request, username):
    if request.method == 'POST':
        you  = get_object_or_404(get_user_model(),username=username)
        me = request.user
        response = {
            'followed': False,
            'count': 0,
        }
        if you.username != me.username:
            if you.followers.filter(username=me.username).exists():
                you.followers.remove(me)
                response['count'] = you.followers.count()
            else:
                you.followers.add(me)
                response['followed'] = True
                response['count'] = you.followers.count()
        
        
        return JsonResponse(response)
    return redirect('accounts/login/')

@require_POST
@login_required
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
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/new_update.html', {'form': form})

@require_http_methods(['POST', 'GET'])
@login_required
def new_update(request, username):
    you  = get_object_or_404(get_user_model(),username=username)
    me = request.user
    if you.username == me.username:
        if request.method == 'GET':
            form = CustomUserChangeForm(instance = you)
            pw_form = CustomPasswordChangeForm(request.user)
            context = {
                'form': form,
                'pw_form': pw_form,
            }
            return render(request, 'accounts/new_update.html', context)
        elif request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=you)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile', you.username)
            context = {
                'form': form
            }
            return render(request, 'accounts/new_update.html', context)
    return redirect('accounts:profile', username)



def profile(request, username):
    user = User.objects.get(username=username)
    
    feeds = user.user_feeds.all().order_by('-id')
    bk_feeds = user.bk_feed.all()
    tag_feeds = user.tag_feeds.all()
    context = {
        'user':user,
        'feeds': feeds,
        'bk_feeds': bk_feeds,
        'tag_feeds': tag_feeds,
    }
    return render(request,'accounts/new_profile.html',context)
