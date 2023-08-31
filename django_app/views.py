from django.shortcuts import render
from django.shortcuts import render
from django_app.models import Article
from .models import Person

# Create your views here.

def index(request):
    return render(request, 'django_app/index.html')

def home(request):
    context = {'data': 'some_data'}  

    return render(request, 'django_app/home.html', context)

def People_list(request):
    people = Person.objects.all()
    context = {'people' : people}
    return render(request, 'match.html', context)
