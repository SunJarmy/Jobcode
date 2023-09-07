from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'age', 'avatar']