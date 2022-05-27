from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/received_money.json'.format(path), 'r') as f:
    data = json.load(f)

e1=[]
for i in range(0,len(data)):
    e=data[i]
    e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/purchase?minorversion=14"

for i in range(0,len(e1)):
    e2={}
    e3={'Line':[]}
    e4={}
    e5={}
    e6={}
    
    e4['Amount']=e1[i]['Payer']
    e4['DetailType']='AccountBasedExpenseLineDetail'
    
    e5['name']=e1[i]['Payer']
    
   
    e7['PaymentType']=e1[i]['PaymentMethod']
    
    
    e8['name']=e1[i]['Deposit_Into']
    e8['Line'].append(e6)
    
    payload = json.dumps(e2)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)