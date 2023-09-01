from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/django_app/user/')
    
    else:
        form = SignupForm()

    param = {
        'form': form
    }

    return render(request, 'django_app/signup.html', param)
    

def login_view(request):
    if request.method == 'POST':
        next = request.POST['next']
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect('/django_app/user/')
            
    else:
        form = LoginForm()

    param = {
        'form' : form
    }

    return render(request, 'django_app/login.html', param)


@login_required
def user_view(request):
    user = request.user

    params = {
        'username': user.username
    }
    return render(request, 'django_app/user.html', params)

def logout_view(request):
    logout(request)
    return redirect('/django_app/login/')
