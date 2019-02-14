from django.shortcuts import render
from datetime import datetime
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

# 우리 헤어지는 시간 출력하기 - 2월 28일까지 남은 시간
def bye(request):
    today = datetime.now()
    goodbye = datetime(2019, 2, 28, 18, 00)
    remain = goodbye - today
    return render(request, 'utilities/bye.html', {'today': today, 'goodbye': goodbye, 'remain' : remain})

# 우리 1학기 졸업시간까지 남은 날짜 출력하기 - 5월 18일까지 남은 시간
def graduation(request):
    today = datetime(2019, 2, 14)
    goodbye = datetime(2019, 5, 18)
    # today = datetime.now()
    # goodbye = datetime(2019, 5, 18, 18, 00)
    days = goodbye - today
    return render(request, 'utilities/graduation.html', {'today': today,'goodbye': goodbye, 'days' : days})
    
# Lorem Picsum 활용하여 랜덤 이미지 출력하기
def imagepick(request):
    return render(request, 'utilities/imagepick.html')

# 오늘 시간 및 날씨 정보 알려주기(지금 살고 있는 기준으로)
def today(request):
    today = datetime.now()

    url = "https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID=50ab815ce98dcf57d58d4547ccd3dbef"
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

# artii를 활용하여 art로 만들어서 출력해주기
def ascii_make(request):
    data = request.GET.get('data')
    fonts = request.GET.get('fonts')
    url = f"http://artii.herokuapp.com/make?text={data}&font={fonts}"
    show = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'show': show})

# 영어 번역을 위한 한국어 입력받기
def original(request):
    return render(request, 'utilities/original.html')

# papago 활용하여 한-영 번역 해주기
def translated(request):
    word = requests.GET.get('word')
    naver_client_id = os.getenv("VdaDzu1w6SJRN96h2EuZ")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": text[4:]
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'result': result})