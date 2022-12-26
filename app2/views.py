from django.shortcuts import render
from django.http import HttpResponse

def second(request):
    return HttpResponse('<marquee><h1>I am living in banglore marathahalli.</h1></marquee>')
