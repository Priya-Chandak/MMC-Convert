import json
import requests
from static import *


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/GeneralLedger/GeneralJournal"


response = requests.request("GET", url, headers=headers, data=payload)

a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {"is_credit_debit": []}
    e['Referrence_No'] = a['Items'][i]["DisplayID"]
    e['Date'] = a['Items'][i]["DateOccurred"]

    for j in range(0, len(a['Items'][i]['Lines'])):
        e['Account_Name'] = a['Items'][i]['Lines'][j]['Account']['Name']
        e["is_credit_debit"].append(
            {"Amount": a['Items'][i]['Lines'][j]['Amount'], "IsCredit": a['Items'][i]['Lines'][j]['IsCredit']})

    arr.append(e)

print(arr)

path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/journal.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
