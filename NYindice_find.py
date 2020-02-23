from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


DB = db.indice.find()[0]
#어차피 다 가져와서 API로 뿌릴거라면 굳이 for문을 쓰지 않아도 됨
Sdata = DB['S&P']
Ddata = DB['DOW']
Ndata = DB['NDQ']

print (DB)


'''for item in data :
    date  =  item['date']
    value =  item['value']
    print(date, ":", value,data)'''
#print(DB['S&P'][0]['date'],DB['S&P'][0]['value'])
#print(DB['DOW'][0]['date'])

#for Sval in Svals:






#  { 'S&P' : [{리스트:안에딕셔너리},{리스트2:안에딕셔너리2}],
#    'DOW' :[{리스트3:안에딕셔너리3},{리스트4:안에딕셔너리4}],
#    'NDQ' :[{리스트5:안에딕셔너리6},{리스트7:안에딕셔너리8}] }
# 각 지수별로 이루어진 큰 딕셔너리 안에 {date:value}가 리스트
