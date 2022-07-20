import random

rain_foods = "짬뽕, 파전, 수제비. 홍합탕, 주꾸미볶음, 삼겹살, 해물탕, 매운탕, 김치찌개".split(',')
pmhigh_foods = "미역국, 콩나물국밥, 곱창, 파스타, 초밥, 김밥, 냉면, 우동, 떡볶이".split(',')

def get_foods_list(weather,dust_pm10, dust_pm20):
    
    if weather != '0':
        recommand_state = 'Case1'
        # random.sample(x, k=len(x)) 무작위로 리스트 섞기
        foods_list = random.sample(rain_foods, k = len(rain_foods))
    elif dust_pm10 == '매우나쁨' or dust_pm20 == '매우나쁨' :
        recommand_state = 'Case2'
        foods_list = random.sample(pmhigh_foods, k=len(pmhigh_foods))
    else:
        recommand_state = 'Case3'
        foods_list = ['']
    
    return recommand_state, foods_list

