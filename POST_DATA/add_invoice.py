from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/item_invoice.json'.format(path), 'r') as f:
    data = json.load(f)

e1=data[0:2]
# for i in range(0,len(data)):
#     e=data[i]
#     e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/invoice?minorversion=14"

for i in range(0,len(e1)):
    e2={'Line':[]}
    e3={}
    e4={}
    e5={}
    e6={}
    e7={}
    
    e2['Amount']=e1[i]['TotalAmount']
    e2['DetailType']='SalesItemLineDetail'
    
    e4['value']=e1[i]['Account_ID']
    e4['name']=e1[i]['Account_Name']
    
    e5['ItemRef'] = e4
    e6['SalesItemLineDetail']=e5
    
    e7['value'] = e1[i]['UID']
    
    e2['Line'].append(e6)
    e2['CustomerRef']=e7
    
    print(e2)
    
    payload = json.dumps(e3)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)