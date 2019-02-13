from django.shortcuts import render, HttpResponse
from pprint import pprint

# Create your views here.
def index(request):
    print(request)
    print(type(request))
    pprint(request.META)
    return HttpResponse('Welcome to Django!')