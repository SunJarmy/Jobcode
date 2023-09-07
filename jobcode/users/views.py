from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomUserCreationForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edit_profile')  # Перенаправляем на страницу редактирования профиля после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})


def profile(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None
    return render(request, 'registration/profile.html', {'profile': profile})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')
