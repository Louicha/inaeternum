from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Your Email Address')
    date_of_birth = forms.DateField(label='Date of Birth')


class ProfileSettingsForm(forms):
    guest_list = forms.CharField(label='Guest List (one per line)')
    words_of_cheer = forms.CharField(label='Words of Cheer')
