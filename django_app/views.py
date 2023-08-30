from django.shortcuts import render
from django.http import JsonResponse
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Create your views here.

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