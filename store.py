import urllib

def naver_local_search(query, display):
    ncreds = {
    "client_id": "<private id>",      
    "client_secret" : "<private secret>"
    }
    nheaders = {
    "X-Naver-Client-Id" : ncreds.get('client_id'),
    "X-Naver-Client-Secret" : ncreds.get('client_secret')
    }
    naver_local_url = "https://openapi.naver.com/v1/search/local.json?"

    res = requests.get(naver_local_url + params, headers=nheaders)

    places = res.json().get('items')

    return places

weather = data.get('weather').get('code')
dust_pm10 = data.get('dust').get('PM10').get("state")
dust_pm20 = data.get('dust').get('PM2.5').get("state")

weather_state, foods_list = get_foods_list(weather, dust_pm10, dust_pm20)
params_format = "sort=comment&query="

location = "광주 동명동"

recommands = []
for food in foods_list:
    query= location + " " + food + " 맛집"
    params = "sort=comment" \
              + "&query=" + query \
              + "&display=" + '5'

    result_list = naver_local_search(query, 3)

    if len(result_list) > 0:
        if weather_state == 'Case3':
            recommands = result_list
            break
        else:
            recommands.append(result_list[0])
    else:
        print("검색 결과 없음")

    if len(recommands) == 3:
        break

print(recommands)
