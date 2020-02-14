import requests

SP5 = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=SP500&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-02-01')
DOW = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=DJIA&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-02-01')
NDQ = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=NASDAQCOM&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-02-01')

Sjson = SP5.json()
Djson = DOW.json()
Njson = NDQ.json()

Svals = Sjson['observations']
for Sval in Svals :
    if Sval['date']=="2020-02-12" :
        print(Sval['value'])

Dvals = Djson['observations']
for Dval in Dvals :
    if Dval['date']=="2020-02-12" :
        print(Dval['value'])

Nvals = Njson['observations']
for Nval in Nvals :
    if Nval['date']=="2020-02-12" :
        print(Nval['value'])




