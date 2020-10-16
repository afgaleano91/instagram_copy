"""CopyInstagram views Module."""

from django.http import HttpResponse

from datetime import datetime

def hello_world(request):
    '''return greeting'''
    now = datetime.now().strftime('%b %dth, %Y -%H:%M hrs')
    return HttpResponse(f'Hi!, Current time server is {now}')

def hi(request):
    '''new greeting'''
    return HttpResponse('Esta es una nueva url bro :v')