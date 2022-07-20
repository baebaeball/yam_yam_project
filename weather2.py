import requests
import json
import datetime
from datetime import date, datetime, timedelta
vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

service_key = "<private key>"

now = datetime.now()
today = datetime.today()
yesterday = date.today() - timedelta(days=1)
today_date = today.strftime("%Y%m%d")
yesterday_date = yesterday.strftime('%Y%m%d')
if now.hour<2 or (now.hour==2 and now.minute<=10):
    base_date=yesterday_date
    base_time="2300"
elif now.hour<5 or (now.hour==5 and now.minute<=10):
    base_date=today_date
    base_time="0200"
elif now.hour<8 or (now.hour==8 and now.minute<=10):
    base_date=today_date
    base_time="0500"
elif now.hour<11 or (now.hour==11 and now.minute<=10):
    base_date=today_date
    base_time="0800"
elif now.hour<14 or (now.hour==14 and now.minute<=10):
    base_date=today_date
    base_time="1100"
elif now.hour<17 or (now.hour==17 and now.minute<=10):
    base_date=today_date
    base_time="1400"
elif now.hour<20 or (now.hour==20 and now.minute<=10):
    base_date=today_date
    base_time="1700" 
elif now.hour<23 or (now.hour==23 and now.minute<=10):
    base_date=today_date
    base_time="2000"
else:
    base_date=today_date
    base_time="2300"


nx = "58"
ny = "74"

payload = "serviceKey=" + service_key + "&" +\
    "dataType=json" + "&" + \
    "base_date=" + base_date + "&" + \
    "base_time=" + base_time + "&" + \
    "nx=" + nx + "&" + \
    "ny=" + ny

pty_code = { "0": "없음", "1" : "비", "2" : "비/눈", "3":"눈", "4":"소나기", "5":"빗방울", "6":"빗방울/눈날림", "7":"눈날림"}

data = dict()
data['date'] = base_date
weather = dict()

res = requests.get(vilage_weather_url + payload)
try:
    items = res.json().get('response').get('body').get('items')
    for item in items['item']:
        if item['category'] == 'TMP':
            weather['tmp'] = item['fcstValue']

        if item['category'] == 'PTY':
            weather['code'] = item['fcstValue']
            weather['state'] = pty_code[item['fcstValue']]
except:
    print("날씨 정보 가져오기 실패 : ", res.text)

data['weather'] = weather
print(data['weather'])
