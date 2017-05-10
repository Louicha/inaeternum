import os

from django.shortcuts import render, HttpResponse

# Create your views here.
from inaeternum.settings import BASE_DIR


def index(request):
    return render(request, os.path.join('polls', 'static', 'StartInformation.html'))
    # return render(request, '../code/StartInformation.html', {})
    # return HttpResponse('Hello World')


def register(request):
    return HttpResponse('Can we just pretend that there\'s a register form on this page?<br>kthxbye')


"""
don't even ask.
TODO: clean this up one day in the far future after I've received enough questions about it
<20:24:15> "Attila": .-.
<20:24:20> "kageru": ._.
<20:24:21> "Attila": ._.
<20:24:25> "Attila": .-.
<20:24:29> "Attila": -.-
<20:24:34> "Attila": .________.
<20:24:36> "kageru": .__.
<20:24:40> "Attila": *_____________*
<20:24:42> "kageru": >.<
<20:24:51> "Attila": ;>
"""
