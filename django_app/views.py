from django.shortcuts import render
from django.http import JsonResponse
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import dayregister
from django.shortcuts import render, redirect
from django.db.models import Q

def get_calendar_events(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=8001) 
    
    service = build('calendar', 'v3', credentials=creds)
    
    events_result = service.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])
    
    return JsonResponse({"events": events})

def index(request):
    return render(request, 'django_app/index.html')

###########ログイン関係###########

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

###################マッチング###################

def check_date_and_name(request):
    if request.method == "POST":
        date_input = request.POST.get("dateInput")
        
        if date_input == "":
            return render(request, "django_app/date_matching.html", {"day": "入力なし"})
        
        # データベースから日付を検索
        matching_bookings = dayregister.objects.filter(Q(date_1=date_input) | Q(date_2=date_input) | Q(date_3=date_input))
        
        if matching_bookings.exists():
            matching_names = [booking.user.username for booking in matching_bookings]  # ユーザー名を取得
        else:
            matching_names = None
        
        return render(request, "django_app/date_matching.html", {"matching_names": matching_names, "day":date_input})
    
    return render(request, "django_app/date_matching.html", {"matching_names": "", "day": ""})

def day_register_form(request):
    if request.method == 'POST':
        date_1 = request.POST.get('date_1')
        date_2 = request.POST.get('date_2')
        date_3 = request.POST.get('date_3')
        amount = request.POST.get('amount')
        
        user = request.user  

        dayregister.objects.filter(user=user).delete()

        booking = dayregister(user=user, date_1=date_1, date_2=date_2, date_3=date_3, amount=amount)
        booking.save()
        
        return redirect('register_check')
    
    registering = dayregister.objects.filter(user=request.user)
    return render(request, 'django_app/day_register_form.html', {'registering': registering})


def register_check(request):
    registering = dayregister.objects.filter(user=request.user)
    return render(request, 'django_app/register_check.html', {'registering': registering})

###################
