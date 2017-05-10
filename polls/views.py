import os

from django.shortcuts import render_to_response

# Create your views here.
from inaeternum.settings import BASE_DIR


def index(request):
    return render_to_response(os.path.join(BASE_DIR,'code','StartInformation.html'))
    #return render(request, '../code/StartInformation.html', {})
    #return HttpResponse('Hello World')
