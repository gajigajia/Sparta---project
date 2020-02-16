import requests

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

SP5 = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=SP500&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')
DOW = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=DJIA&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')
NDQ = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=NASDAQCOM&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')

Sjson = SP5.json()
Djson = DOW.json()
Njson = NDQ.json()

Svals = Sjson['observations']
Sresult = dict()
for Sval in Svals :
    Sresult = {'date':Sval['date'], 'value':Sval['value']}

    db.SP500.insert_one(Sresult)

Dvals = Djson['observations']
Dresult = dict()
for Dval in Dvals:
    Dresult = {'date': Dval['date'], 'value': Dval['value']}

    db.DJIA.insert_one(Dresult)

Nvals = Njson['observations']
Nresult = dict()
for Nval in Nvals :
    Nresult = {'date': Nval['date'], 'value': Nval['value']}

    db.NASDAQ.insert_one(Nresult)












