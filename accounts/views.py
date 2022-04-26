from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import User

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

def profile(request,pk):
    user = User.objects.get(pk=pk)
    context = {
        'user':user,
    }
    return render(request,'accounts/profile.html',context)
