from pymongo import mongo_client


uri = "mongodb://localhost:27017"
mgCilent = mongo_client.MongoClient(uri)
print(mgCilent)

mgDb = mgCilent["movegunDB"]
dbNames = mgCilent.list_database_names()

mgCol = mgDb["customers"]
colNames = mgDb.list_collection_names()

myDic = {"name":"movegun",
         "addr":"incheon",
         "age":20    
}

x = mgCol.insert_one(myDic)
print(x.inserted_id)

if "movegunDB" in dbNames:
    print("movegunDB 존재")