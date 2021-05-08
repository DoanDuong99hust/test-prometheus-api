from time import sleep

import pymongo
from database import getServerStatus as status

myclient = pymongo.MongoClient("mongodb://192.168.100.137:27017/")
mydb = myclient["test-prometheus"]

# cpu
cpucoll = mydb["Worker"]
server_status = mydb["status"]
# cpucoll.save(status.get_worker())

cols = cpucoll.find()
# for i in cols:
#     print(i)

while 1 :
    server_status.save(status.get_machine_status())
    for data in server_status.find():
        print(data)
    print("---------------")
    sleep(10)
