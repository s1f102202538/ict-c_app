from django.urls import path
from . import views

urlpatterns = [
    path("", views.check_date_and_name, name="check_date_and_name"),
]
