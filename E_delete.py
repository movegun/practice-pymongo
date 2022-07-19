from certifi import where
from pymongo import mongo_client
from pyparsing import col

uri = "mongodb://localhost:27017"
mgCilent = mongo_client.MongoClient(uri)
db = mgCilent["movegunDB"]
coll = db["studentInfo"]

import datetime as dt
dt_now = dt.datetime.now()
dt_now = dt_now.strftime('%Y/%m/%d %H:%M:%S')

dics = [
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
]

coll.drop()
coll.insert_many(dics)

# 1개 삭제 
where = {"name":"마길동"}
deleted_doc = coll.delete_one(where)
print("where 에 의한 삭제 doc :",deleted_doc.deleted_count,"개")

# 여러개 삭제
where1 = {"addr":{"$lt":"서"}}      #where addr<'서'
deleted_object1 = coll.delete_many(where1)
print("where1 에 의한 삭제 docs :",deleted_object1.deleted_count,"개")

where2 = {"addr":{"$regex":"^서"}}  #wherea addr like '서%'
deleted_object2 = coll.delete_many(where2)
print("where2 에 의한 삭제 docs :",deleted_object2.deleted_count,"개")

#확인
docs = coll.find()
for doc in docs:
    print(doc)