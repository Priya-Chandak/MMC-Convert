import json
import requests
from static import *

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Banking/ReceiveMoneyTxn"


response = requests.request("GET", url, headers=headers, data=payload)


a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}
    e['Deposit_Into'] = a['Items'][i]["Account"]['Name']
    e['Notes'] = a['Items'][i]['Memo']
    e['Date'] = a['Items'][i]['Date']
    e['Reference_No'] = a['Items'][i]['ReceiptNumber']
    e['TotalTax'] = a['Items'][i]['TotalTax']
    e['Is_Tax_Inclusive'] = a['Items'][i]['IsTaxInclusive']

    for j in range(0, len(a['Items'][i]['Lines'])):
        e['Payer'] = a['Items'][i]['Lines'][j]['Account']['Name']
        e['Tax_Code'] = a['Items'][i]['Lines'][j]['TaxCode']['Code']

    e['Amount'] = a['Items'][i]['AmountReceived']

    arr.append(e)
print(arr)

path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open(
    "{}/received_money.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
