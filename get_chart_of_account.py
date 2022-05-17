import json
import requests
from static import *


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/GeneralLedger/Account"


response = requests.request("GET", url, headers=headers, data=payload)


a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}
    e['Account_Type'] = a['Items'][i]['Type']
    e['Name'] = a['Items'][i]['Name']
    e['Detail_Type'] = a['Items'][i]['Name']
    e['Description'] = a['Items'][i]['Description']

    if a['Items'][i]['TaxCode'] != None:
        e['Tax_Code'] = a['Items'][i]['TaxCode']['Code']
    else:
        e['Tax_Code'] = '--'

    arr.append(e)


path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/chart_of_account.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
