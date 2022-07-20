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
res = requests.get(vilage_weather_url + payload)
try:
    items = res.json().get('response').get('body').get('items')
    print(items)
except:
    print("날씨 정보 요청 실패 : ", res.text)

