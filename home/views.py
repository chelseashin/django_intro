from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')
    
def dinner(request):
    menus = ['치킨', '삼겹살', '비빔밥', '파스타', '피자']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick})