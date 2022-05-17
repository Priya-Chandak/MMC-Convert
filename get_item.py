import json
import requests
from static import *


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Sale/Invoice/Item"


response = requests.request("GET", url, headers=headers, data=payload)


print(response.text)

a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}
    e['UID'] = a['Items'][i]["UID"]
    e['TotalAmount'] = a['Items'][i]['TotalAmount']
    e['Customer_Name'] = a['Items'][i]['Customer']['Name']
    e['DiscountDate'] = a['Items'][i]['Terms']['DiscountDate']
    e['BalanceDueDate'] = a['Items'][i]['Terms']['BalanceDueDate']

    for j in range(0, len(a['Items'][i]['Lines'])):
        e['Description'] = a['Items'][i]['Lines'][j]['Description']

    arr.append(e)

path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/item.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
