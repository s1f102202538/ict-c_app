from django.urls import path
from . import views

urlpatterns = [
    path('get_calendar_events/', views.get_calendar_events, name='get_calendar_events'),
    path("", views.check_date_and_name, name="check_date_and_name"),
]
