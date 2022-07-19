from pymongo import mongo_client

uri = "mongodb://localhost:27017"
mgCilent = mongo_client.MongoClient(uri)
db = mgCilent["movegunDB"]
coll = db["studentInfo"]


#import datetime as dt
#dt_now = dt.datetime.now()
#dt_now = dt_now.strftime('%Y/%m/%d %H:%M:%S')

'''dics = [
  { "_id":1, "name": "가길동", "addr": "서울", "rdate":dt_now},
  { "_id":2, "name": "나길동", "addr": "경기", "rdate":dt_now},
  { "_id":3, "name": "다길동", "addr": "부산", "rdate":dt_now},
  { "_id":4, "name": "라길동", "addr": "인천", "rdate":dt_now},
  { "_id":5, "name": "마길동", "addr": "대구", "rdate":dt_now},
  { "_id":6, "name": "바길동", "addr": "광주", "rdate":dt_now},
  { "_id":7, "name": "사길동", "addr": "대전", "rdate":dt_now},
  { "_id":8, "name": "아길동", "addr": "울산", "rdate":dt_now},
  { "_id":9, "name": "자길동", "addr": "창원", "rdate":dt_now},
  { "_id":10, "name": "차길동", "addr": "청주", "rdate":dt_now}
]'''

#inserted_object = coll.insert_many(dics)
#print("x.inserted_ids : ", inserted_object.inserted_ids)

# 모든 컬럼 ( _id ~~~~~~~~ rdate 까지 select)
docs = coll.find()
for dic in docs:
  print(dic)
print("-------------------------------------------------------------------------------------")

# 결과를 반환할 때 포함과 제외의 혼합을 허용하지 않습니다.결과를 반환할 때 포함과 제외의 혼합을 허용하지 않습니다.
docs = coll.find({},{"_id":1,"name":0,"addr":0,"rdate":0})
for dic in docs:
  print(dic)