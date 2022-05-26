from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/customer.json'.format(path), 'r') as f:
    data = json.load(f)

e1=[]
for i in range(0,len(data)):
    e=data[i]
    e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/customer?minorversion=14"

for i in range(0, len(e1)):
    
    e2 = {}
    e3 = {}
    e4 = {}
    e5 = {}
    e2['Notes']=e1[i]['Notes']
    e2['DisplayName']=e1[i]['Company_Name']
    
    if e1[i]['Addresses'] != '--':
        e3['Line1'] = e1[i]['Addresses'][0]['Street']
        e3['City'] = e1[i]['Addresses'][0]['City']
        e3['Country'] = e1[i]['Addresses'][0]['Country']
        e3['CountrySubDivisionCode'] = e1[i]['Addresses'][0]['PostCode']
        e3['PostalCode'] = e1[i]['Addresses'][0]['PostCode']
    else:
        pass
    
    e4['FreeFormNumber'] = e1[i]['Addresses'][0]['Phone1']
    e5['Address'] = e1[i]['Addresses'][0]['Email']
    e2['BillAddr'] = e3
    e2['PrimaryPhone'] = e4
    
    e2['PrimaryEmailAddr'] = e5

    payload = json.dumps(e2)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)    
