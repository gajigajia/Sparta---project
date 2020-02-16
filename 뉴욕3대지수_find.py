from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


find_index = db.DJIA.find_one({'date':'2020-02-14'},{'_id':0})
print(find_index)










