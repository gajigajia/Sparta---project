import requests # requests 라이브러리 설치 필요

NK = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=NIKKEI225&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-02-01')

NKjson = NK.json()

NKvals = NKjson['observations']
for NKval in NKvals :
    if NKval['date']=="2020-02-12" :
        print(NKval['value'])
