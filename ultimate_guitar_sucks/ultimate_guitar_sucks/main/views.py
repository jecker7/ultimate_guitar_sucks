import csv
import json
import os
import datetime
import requests as re
from bs4 import BeautifulSoup as bs


from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings as django_settings
from django.utils.encoding import smart_str
from django.contrib.auth.decorators import login_required


from .forms import TabForm




def main(request):
    template = 'main/home.html'

    if not requestmethod == 'POST':
        return render(request, template, {'url_form': URLForm()})

    url_form = URLForm(request.POST)

    return render(request, template,
                  {'tab_output': tab_output})

def get_tab(url):

    page = re.get(url).content


