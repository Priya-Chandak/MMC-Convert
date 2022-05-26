import requests
import json
from static import headers

url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/item?minorversion=14"

path = input("path :")
with open('{}/item.json'.format(path), 'r') as f:
    data = json.load(f)

e1=data[0:5]

for i in range(0,len(e1)):
    e2={}
    e3={}
    e4={}
    e5={}
    e2['Name'] = e1[i]['Name']
    e2['Type'] = 'NA'
    e2['TrackQtyOnHand'] = e1[i]['TrackQtyOnHand']
    e2['QtyOnHand'] = '1'
    e2['InvStartDate'] = e1[i]['LastModified']
    
    e3['Value'] = e1[i]['Income_Account_ID']
    e3['Name'] = e1[i]['Income_Account_Name']
    
    e4['value']= e1[i]['Expense_Account_ID']
    e4['Name']= e1[i]['Expense_Account_Name']
    
    e5['value']= e1[i]['Asset_Account_ID']
    e5['Name']= e1[i]['Asset_Account_Name']
    
    e2['IncomeAccountRef'] = e3
    e2['ExpenseAccountRef']=e4
    e2['AssetAccountRef']=e5


    payload = json.dumps(e2)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response)
    print(response.text)

    