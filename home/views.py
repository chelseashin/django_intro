from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')
    
def dinner(request):
    menus = ['치킨', '삼겹살', '비빔밥', '파스타', '피자']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, number):
    result = number ** 3
    return render(request, 'cube.html', {'number': number, 'result': result})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html',{'data' : data})
    
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname' : nickname, 'pwd' : pwd})