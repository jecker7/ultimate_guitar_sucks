import csv
import json
import os
import datetime
import requests
import re
from bs4 import BeautifulSoup as bs


from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings as django_settings
from django.utils.encoding import smart_str
from django.contrib.auth.decorators import login_required

from ascii_tab_to_svg import TabScraper
from .forms import URLForm

def main(request):
    """
    Main method to handle views for our single page.
    Passes a URLForm to the page, the user enters in a URL,
    we handle the URL to process the tab, then pass the tab as
    an object to our home.html template
    :param request:
    :return:
    """
    template = 'main/home.html'

    if not request.method == 'POST':
        return render(request, template, {'url_form': URLForm()})

    url_form = URLForm(request.POST)

    if not url_form.is_valid():
        print('form problem')
        print(url_form.errors)
        return render(request, template, {'url_form': url_form})

    url = url_form.cleaned_data['url']
    # will finish refactoring this later once logic is done
    scraper = TabScraper(tab)
    tab_output = None
    return render(request, template,
                  {'tab_output': tab_output})

def display_tab(tab):
    """
    Display our tab in the browser as SVG using VexTab (for now)
    :param tab:
    :return: template
    """

    template = 'main/home.html'

    return render(request, template,
                  {'tab_output': tab_output})


