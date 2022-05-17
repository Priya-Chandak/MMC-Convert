import json
import requests
from static import *

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/GeneralLedger/Account"


response = requests.request("GET", url, headers=headers, data=payload)


a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}
    e['Account_Name'] = a['Items'][i]['Name']

    if a['Items'][i]['CurrentBalance'] < 0:
        e['Credit'] = a['Items'][i]['CurrentBalance']
    else:
        e['Debit'] = a['Items'][i]['CurrentBalance']

    arr.append(e)


path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/trial_balance.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
