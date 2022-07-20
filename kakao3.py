contents = []
template = {
    "object_type" : "list",
    "header_title" : "현재 날씨에 따른 음식 추천",
    "header_link" : {
        "web_url": weather_url,
        "mobile_web_url" : weather_url
    },
    "contents" : contents,
    "buttons" : [
        {
            "title" : "날씨 정보 상세보기",
            "link" : {
                "web_url": weather_url,
                "mobile_web_url" : weather_url
            }
        }
    ],
}

for place in recommands:
    title = place.get('title') 
    title = title.replace('<b>','').replace('</b>','')

    category = place.get('category')
    telephone = place.get('telephone')
    address = place.get('address')

    enc_address = address + ' ' + title
    query = "query=" + enc_address

    if '카페' in category:
        image_url = "https://freesvg.org/img/pitr_Coffee_cup_icon.png"
    else:
        image_url = "https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill"

    if telephone:
        title = title + "\ntel) " + telephone

    content = {
        "title": "[" + category + "] " + title,
        "description": ' '.join(address.split()[1:]),
        "image_url": image_url,
        "image_width": 50, "image_height": 50,
        "link": {
            "web_url": "https://search.naver.com/search.naver?" + query,
            "mobile_web_url": "https://search.naver.com/search.naver?" + query
        }
    }

    contents.append(content)

payload = {
    "template_object" : json.dumps(template)
}

res = requests.post(kakaotalk_template_url, data=payload, headers=kheaders)
if res.json().get('result_code') == 0:
    print('맛집 정보 성공적으로 보냈습니다.')
else:
    print('맛집 정보 성공적으로 보내지 못했습니다. 오류메시지 : ', res.json())
