from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def dt(request):
    msg='<h1>good evening</h1>'
    date=datetime.datetime.now()
    msg+='<h1>now the server time is'+str(date)+'</h1>'

    return HttpResponse(msg)
def ben(request):
    s='<h1>hi sureh</h1>'
    return HttpResponse(s)

def timeInfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1>hi the wish was'
    if h<12:
        msg+='good morning'

    elif h<16:
        msg+='good noon'

    elif h<19:
        msg+='good evening'

    else :
        msg+='good night'

    msg=msg+'</h1><hr>'
    msg+='<h1>now the server time is'+str(date)+'</h1>'

    return HttpResponse(msg)
