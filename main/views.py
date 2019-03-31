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


from forms import URLForm

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

    tab = get_tab(url)

    tab_output = None
    return render(request, template,
                  {'tab_output': tab_output})

def process_tab(tab):
    """
    Function to process our tab. Not sure how we'll be doing this, so leaving
    empty for now

    One simple start can be to just join the entire tab on /n characters, so we have a
    continuous unbroken represenation of our tab in ASCII. This can then be turned into a
    simple JSON object, or just passed as a string to be handled on the front-end (somehow).

    :return:
    """

    # this shouldn't be too difficult, each line of the tab begins with the corresponding note of the string
    # e.g. 'a', 'b', etc. and then '|', and terminates with '\n'. SO, all we have to do, is join each string-line:
    # .join('b|','\nb|'), etc. etc.



def get_tab(url):
    """
    Function to get our tab from the url specified. Uses one pattern now, must be tested
    across more tabs and patterns to ensure that we grab the right tab for our link
    :param url:
    :return:
    """
    # making our soup with page content
    page = bs(requests.get(url).content, features='lxml')

    # this pattern should work for at least some UG pages:
    pattern = 'content":"[^"]*'
    m = re.search(pattern, page.prettify())
    tab = m.group(0)
    return tab
