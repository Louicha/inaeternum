import os

from django.shortcuts import render

# Create your views here.
from inaeternum.settings import BASE_DIR


def index(request):
    return render(request, os.path.join('static', 'StartInformation.html'))
    # return render(request, '../code/StartInformation.html', {})
    # return HttpResponse('Hello World')
