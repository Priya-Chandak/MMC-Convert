import json
import requests
from static import *


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Sale/Invoice/Item"


response = requests.request("GET", url, headers=headers, data=payload)

a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}
    e['UID'] = a['Items'][i]["UID"]
    e['TotalAmount'] = a['Items'][i]['TotalAmount']
    e['Customer_Name'] = a['Items'][i]['Customer']['Name']
    e['Invoice_Number'] = a['Items'][i]['Number']
    e['Date'] = a['Items'][i]['Date']
    e['Due_Date'] = a['Items'][i]['Terms']['DueDate']

    for j in range(0, len(a['Items'][i]['Lines'])):
        e['Description'] = a['Items'][i]['Lines'][j]['Description']
        e['Unit_Price'] = a['Items'][i]['Lines'][j]['UnitPrice']
        e['Total'] = a['Items'][i]['Lines'][j]['Total']
        e['Unit_Count'] = a['Items'][i]['Lines'][j]['UnitCount']
        e['Item_Name'] = a['Items'][i]['Lines'][j]['Item']['Name']

    arr.append(e)


path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open(
    "{}/invoice.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
