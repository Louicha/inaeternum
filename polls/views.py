import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
# from inaeternum.settings import BASE_DIR
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileSettingsForm
from django.views.generic.edit import UpdateView
from polls.models import UserProfile


def index(request):
    return render(request, os.path.join('polls', 'static', 'StartInformation.html'))


def register(request):
    # form data is send to the server
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Registration successful')
    # if GET (or any other method), we'll create a blank form
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class settings(UpdateView):
    template_name = 'registration/profile.html'
    model = UserProfile
    fields = ['cheer', 'guest_list']
    success_url = '/accounts/profile/'

    def get_object(self, qs=None):
        return UserProfile.objects.for_user(self.request.user)

"""
@login_required
def settings(request):
    if request.method == 'POST':
        form = ProfileSettingsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/profile/')
    else:
        user_profile = request.user.profile
        form = ProfileSettingsForm(instance=user_profile)
        words_of_cheer = user_profile.cheer
        guest_list = user_profile.guest_list
        context = {
            'words_of_cheer': words_of_cheer,
            'guest_list': guest_list,
            'form': form
        }
        return render(request, 'registration/profile.html', context)
"""