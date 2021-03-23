import json
from methods import PrometheusFunctions
from methods import NodeExporterOverride
from types import SimpleNamespace
import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.100.137:27017/")
mydb = myclient["WorkerStatus"]
list_col = mydb.list_collection_names()
print(list_col)