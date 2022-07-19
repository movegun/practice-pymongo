from pymongo import mongo_client


uri = "mongodb://localhost:27017"
mgCilent = mongo_client.MongoClient(uri)
db = mgCilent["movegunDB"]
coll = db["studentInfo"]

import datetime
dt_now = datetime.datetime.now()
dt_now = dt_now.strftime('%Y/%m/%d %H:%M:%S')
#dt_today = datetime.date.today()
#dt_today = dt_today.strftime('%Y/%m/%d')
print(dt_now)
print("---------------------------------------")
dic1 = {"name":"이동건",
         "addr":"인천",
         "age":26,
         "rdate":dt_now
}
dic2 = {"name":"김민수",
         "addr":"수원",
         "age":27,
         "rdate":dt_now
}
dic3 = {"name":"이창근",
         "addr":"일산",
         "age":27,
         "rdate":dt_now
}
#doc = coll.insert_one(dic1)
#doc = coll.insert_one(dic2)
#doc = coll.insert_one(dic3)
#print("doc.inserted_id : ",doc.inserted_id)
print("---------------------------------------")

#coll.delete_one({'name':'이창근'})

# Select * from coll
for x in coll.find(): # = select
    print(x)
print("---------------------------------------")
# slect * from coll 5개
for x in coll.find().limit(5): # = select
    print(x)

# select * from coll order by name desc
'''for x in coll.find().sort("name",-1):
    print(x)'''

print("---------------------------------------")
'''for x in coll.find().sort("_id",1):
    print(x)'''

#coll.drop()

