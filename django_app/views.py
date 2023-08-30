from django.shortcuts import render
from django.shortcuts import render
from django_app.models import Article

# Create your views here.

def index(request):
    return render(request, 'django_app/index.html')

def home(request):
    context = {'data': 'some_data'}  # コンテキストを辞書で定義

    return render(request, 'django_app/home.html', context)
