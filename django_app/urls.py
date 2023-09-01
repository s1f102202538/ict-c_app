from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('user/', views.user_view, name='user'),
    path('logout/', views.logout_view, name='logout')
]