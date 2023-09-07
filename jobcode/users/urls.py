from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='base'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]