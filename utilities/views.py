from django.shortcuts import render
from datetime import datetime
import requests
import json
import os

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

# 우리 헤어지는 시간 출력하기 - 2월 28일까지 남은 시간
def bye(request):
    today = datetime.now()
    goodbye = datetime(2019, 2, 28, 18, 00)
    remain = (goodbye - today).hours()
    return render(request, 'utilities/bye.html', {'remain' : remain})

# 우리 1학기 졸업시간까지 남은 날짜 출력하기 - 5월 18일까지 남은 시간
def graduation(request):
    today = datetime.now()
    goodbye = datetime(2019, 5, 18)
    days = (goodbye - today).days
    return render(request, 'utilities/graduation.html', {'days' : days})
    
# Lorem Picsum 활용하여 랜덤 이미지 출력하기
def imagepick(request):
    return render(request, 'utilities/imagepick.html')

# 오늘 시간 및 날씨 정보 알려주기(지금 살고 있는 기준으로)
def today(request):
    today = datetime.now()
    WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID={WEATHER_TOKEN}"
    data = requests.get(url).json()
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15)
    min_temp = round(data['main']['temp_min'] - 273.15)
    max_temp = round(data['main']['temp_max'] - 273.15)
    
    return render(request, 'utilities/today.html', 
                {'today': today, 'weather': weather, 'temp': temp, 'min_temp': min_temp, 'max_temp': max_temp})
        
# ascii art를 변환을 위한 text, font 입력받기
def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')

# ascii를 활용하여 art로 만들어서 출력해주기
def ascii_make(request):
    data = request.GET.get('data')
    fonts = request.GET.get('fonts')
    # 반복문으로 풀기 : fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    url = f"http://artii.herokuapp.com/make?text={data}&font={fonts}"
    show = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'show': show})

# 영어 번역을 위한 한국어 입력받기
def original(request):
    return render(request, 'utilities/original.html')

# papago 활용하여 한-영 번역 해주기
def translated(request):
    naver_client_id = os.getenv("PAPAGO_ID_TOKEN")
    naver_client_secret = os.getenv("PAPAGO_PW_TOKEN")
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "PAPAGO_ID_TOKEN": naver_client_id,
        "PAPAGO_PW_TOKEN": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": request.GET.get('text')
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    # print(papago_response)
    reply_text = papago_response
    # reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'reply_text': reply_text})