text = f"""\
# 날씨 정보 ({data['date']})
기온 : {data['weather']['tmp']}
기우 : {data['weather']['state']}
미세먼지 : {data['dust']['PM10']['value']} {data['dust']['PM10']['state']}
초미세먼지 : {data['dust']['PM2.5']['value']} {data['dust']['PM2.5']['state']}
"""

template = {
    "object_type": "text",
    "text": text,
    "link": {
        "web_url": weather_url,
        "mobile_web_url": weather_url
    },
    "button_title": "날씨 상세보기"
}

payload = {
    "template_object" : json.dumps(template)
}

res =requests.post(kakaotalk_template_url, data=payload, headers=kheaders)
if res.json().get('result_code') == 0:
    print('날씨 및 미세먼지 정보 성공적으로 보냈습니다.')
else:
    print('날씨 및 미세먼지 정보 성공적으로 보내지 못했습니다. 오류메시지 : ', res.json())
