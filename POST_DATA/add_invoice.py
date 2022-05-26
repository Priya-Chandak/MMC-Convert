from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/invoice.json'.format(path), 'r') as f:
    data = json.load(f)

e1=[]
for i in range(0,len(data)):
    e=data[i]
    e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/invoice?minorversion=14"

for i in range(0, len(e1)):
    
    e2={'Line':[]}
    e3 = {}
    e4 = {}
    e5 = {}
    e6 = {}
    
    e3['Amount']=e1[i]['TotalAmount']
    if e1[i] in ['Description']:
        e3['DetailType']=e1[i]['Description']
    else:
        pass
    if e1[i] in ['Item_Name']:
        e5['name'] = e1[i]['Item_Name']
    else:
        pass
    if  e1[i] in ['Item_UID']:
        
        e5['value'] = e1[i]['Item_UID']
    else:
        pass
    e6['value'] = e1[i]['Customer_UID']
    
    
    e2['Line']=e3
    e2['Line']['ItemRef']=e5
  
    
    e3['CustomerRef'] = e6

    payload = json.dumps(e3)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)