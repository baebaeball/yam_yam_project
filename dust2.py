import requests
import json
import datetime

dust_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?"

service_key = "<private key>"

payload = "serviceKey=" + service_key + "&" + \
          "returnType=json" + "&" + \
          "sidoName=광주" + "&" + \
          "ver=1.0"

def get_pm10_state(pm10_value):
    if pm10_value <= 30:
        pm10_state = "좋음"
    elif pm10_value <= 80:
        pm10_state = "보통"
    elif pm10_value <= 150:
        pm10_state = "나쁨"
    else:
        pm10_state = "매우나쁨"

    return pm10_state

def get_pm25_state(pm25_value):
    if pm25_value <= 15:
        pm25_state = "좋음"
    elif pm25_value <= 35:
        pm25_state = "보통"
    elif pm25_value <= 75:
        pm25_state = "나쁨"
    else:
        pm25_state = "매우나쁨"

    return pm25_state

res = requests.get(dust_url + payload)
result = res.json()
data = dict()
dust = dict()

if (res.status_code == 200) & (result['response']['header']['resultCode'] == '00'):
    dust['PM10'] = {'value' : int(result['response']['body']['items'][0]['pm10Value'])}
    dust['PM2.5'] = {'value' : int(result['response']['body']['items'][0]['pm25Value'])}
    pm10_value = dust.get('PM10').get('value')
    pm10_state = get_pm10_state(pm10_value)
    pm25_value = dust.get('PM2.5').get('value')
    pm25_state = get_pm25_state(pm25_value)

    dust.get('PM10')['state'] = pm10_state
    dust.get('PM2.5')['state'] = pm25_state
else:
    print("미세먼지 가져오기 실패 : ", result['response']['header']['resultMsg'])

data['dust'] = dust
print(data['dust'])
