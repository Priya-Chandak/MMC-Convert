import json 
import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['MYOB']
information=mydb.item_bill

path=input("Enter the path of file : ")
with open('{}/item_bill.json'.format(path)) as file:
    file_data = json.load(file)
information.insert_many(file_data)