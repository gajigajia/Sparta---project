import requests

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

SP5 = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=SP500&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')
DOW = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=DJIA&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')
NDQ = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=NASDAQCOM&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')

Sjson = SP5.json()
Djson = DOW.json()
Njson = NDQ.json()

Svals = Sjson['observations']
Sresult = list()
for Sval in Svals :
    Sresult.append({'date':Sval['date'], 'value':Sval['value']})

Dvals = Djson['observations']
Dresult = list()
for Dval in Dvals:
    Dresult.append({'date': Dval['date'], 'value': Dval['value']})

Nvals = Njson['observations']
Nresult = list()
for Nval in Nvals :
    Nresult.append({'date': Nval['date'], 'value': Nval['value']})


doc = {
    "S&P": Sresult,
    "DOW": Dresult,
    "NDQ" : Nresult,
}


print(doc)