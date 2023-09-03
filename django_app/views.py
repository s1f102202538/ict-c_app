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

def check_date_and_name(request):
    dataList = [
    { "date": "2023-08-01", "name": "坂村健" },
    { "date": "2023-08-02", "name": "井上円了" },
    { "date": "2023-08-30", "name": "Alice" },
    { "date": "2023-08-30", "name": "ooo" },
    { "date": "2023-08-29", "name": "Bob" },
    { "date": "2023-08-28", "name": "Charlie" },
    { "date": "2023-08-27", "name": "David" },
    { "date": "2023-08-26", "name": "Eva" },
    { "date": "2023-08-25", "name": "Frank" },
    { "date": "2023-08-24", "name": "Grace" },
    { "date": "2023-08-23", "name": "Henry" },
    { "date": "2023-08-22", "name": "Ivy" },
    { "date": "2023-08-21", "name": "Jack" },
    { "date": "2023-08-20", "name": "Karen" },
    { "date": "2023-08-19", "name": "Leo" },
    { "date": "2023-08-18", "name": "Mia" },
    { "date": "2023-08-17", "name": "Nathan" },
    { "date": "2023-08-16", "name": "Olivia" },
    { "date": "2023-08-15", "name": "Paul" },
    { "date": "2023-08-14", "name": "Quinn" },
    { "date": "2023-08-13", "name": "Rachel" },
    { "date": "2023-08-12", "name": "Samuel" },
    { "date": "2023-08-11", "name": "Tina" },
    { "date": "2023-08-10", "name": "Ulysses" },
    { "date": "2023-08-09", "name": "Victoria" },
    { "date": "2023-08-08", "name": "William" },
    { "date": "2023-08-07", "name": "Xander" },
    { "date": "2023-08-06", "name": "Yara" },
    { "date": "2023-08-05", "name": "Zane" },
]
    
    if request.method == "POST":
        dateInput = request.POST.get("dateInput")
        nameInput = request.POST.get("nameInput")
        
        matchingData = [item for item in dataList if item["date"] == dateInput]
        
        if matchingData:
            matching_names = ", ".join(item["name"] + "さん" for item in matchingData)  # ここを変更
            result = f"{nameInput}さんは{matching_names}とマッチしました❤"
        else:
            result = f"{nameInput}さん、誰ともマッチしませんでした😢"
        
        return render(request, "django_app/date_matching.html", {"result": result})
    
    return render(request, "django_app/date_matching.html", {"result": ""})

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