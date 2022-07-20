KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"
KAKAO_APP_KEY = "<private key>"

kakaotalk_template_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
weather_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"

kcreds = {
    "access_token" : "<private token>"
}
kheaders = {
    "Authorization": "Bearer " + kcreds.get('access_token')
}
