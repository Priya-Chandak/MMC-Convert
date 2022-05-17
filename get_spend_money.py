import json
import requests
from static import *


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Banking/SpendMoneyTxn"


response = requests.request("GET", url, headers=headers, data=payload)

a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}

    e['Pay_From'] = a['Items'][i]["Account"]['Name']

    if a['Items'][i]["Contact"] != None:
      e['Pay_To'] = a['Items'][i]["Contact"]['Name']
    else:
      e['Pay_To'] = '--'

    e['Date'] = a['Items'][i]['Date']
    e['Description'] = a['Items'][i]['Memo']
    e['Is_Tax_Inclusive'] = a['Items'][i]['IsTaxInclusive']
    e['Payment_Number'] = a['Items'][i]['PaymentNumber']
    e['Amount_Paid'] = a['Items'][i]['AmountPaid']
    e['Total_Tax'] = a['Items'][i]['TotalTax']

    for j in range(0, len(a['Items'][i]['Lines'])):
        e['TaxCode_UID'] = a['Items'][i]['Lines'][j]['TaxCode']['UID']

    arr.append(e)

print(arr)

path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/spend_money.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
