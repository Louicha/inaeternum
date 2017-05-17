import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
# from inaeternum.settings import BASE_DIR
from django.contrib.auth.forms import UserCreationForm

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
