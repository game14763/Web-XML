import os
from django.conf import settings
import mimetypes
from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return render(request,'index.html')

def download_file(request):
    # fill these variables with real values
    fl_path = '/static/xmls'
    filename = 'gdp_per_co2.xml'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
