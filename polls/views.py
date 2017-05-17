import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
# from inaeternum.settings import BASE_DIR
from .forms import RegisterForm


def index(request):
    return render(request, os.path.join('polls', 'static', 'StartInformation.html'))


def register(request):
    # form data is send to the server
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # TODO: insert into database
            return HttpResponseRedirect('Registration successful')
    # if GET (or any other method), we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
