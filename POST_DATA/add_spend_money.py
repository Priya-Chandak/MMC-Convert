from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/spend_money.json'.format(path), 'r') as f:
    data = json.load(f)

e1=data[0:2]
# for i in range(0,len(data)):
#     e=data[i]
#     e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/deposit?minorversion=14"

for i in range(0,len(e1)):
    e2={'Line':[]}
    e3={}
    e4={}
    e5={}
    e6={}
    
    e3['value']=e1[i]['Pay_to_ID']
    e3['name']=e1[i]['Pay_To']
    
    e4['value']=e1[i]['Account_UID']
    e4['name']=e1[i]['Account_Name']
    
    e5['AccountRef']=e4
    e6['Amount']=e1[i]['Amount_Paid']
    e6['DetailType']='DepositLineDetail'
    e6['DepositLineDetail']=e5
    
    e2['DepositToAccountRef']=e3
    e2['Line'].append(e6)
    
    payload = json.dumps(e2)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)
    
