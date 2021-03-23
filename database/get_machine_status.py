import pymongo
myclient = pymongo.MongoClient("mongodb://192.168.100.137:27017/")

print(myclient.list_database_names())