from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/supplier.json'.format(path), 'r') as f:
    data = json.load(f)

e1=[]
for i in range(0,len(data)):
    e=data[i]
    e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/vendor?minorversion=14"

for i in range(0, len(e1)):
    
    
    e2 = {}
    e3 = {}
    e4 = {}
    e5 = {}
    e6 = {}
    e7 = {}
    
    e2['TaxIdentifier']=e1[i]['TaxIdNumber']
    e2['AcctNum']=e1[i]['Bank_Acc_no']
    e2['Title']=''  
    e2['CompanyName']=e1[i]['CompanyName']
    e2['GivenName']=e1[i]['FirstName']
    e2['FamilyName']=e1[i]['LastName']
    e2['DisplayName']=e1[i]['CompanyName']
    e2['Suffix']=''
    e2['PrintOnCheckName']=e1[i]['CompanyName']
    
    if e1[i] in ['Street']:
        e3['Line1']=e1[i]['Street']
    else:
        pass
 
    e3['Line1'] = ''
    e3['Line1'] = ''
    e3['City']=e1[i]['city']
    e3['Country']=e1[i]['Country']
    e3['CountrySubDivisionCode']=''
    e3['PostalCode']=e1[i]['PostCode']
    
    
     
    if e1[i] in ['Phone']:
        e4['FreeFormNumber']=e1[i]['Phone']
    else:
        e4['FreeFormNumber']=""
    if e1[i] in ['Phone']:
        e5['FreeFormNumber']=e1[i]['Phone']
    else:
        e5['FreeFormNumber']=""

    e6['Address']=e1[i]['Email']
    e7['URI']='https://'+e1[i]['Website']
    
    
    e2['BillAddr'] = e3
    e2['PrimaryPhone']=e4
    e2['Mobile']=e5
    e2['PrimaryEmailAddr']=e6
    e2['WebAddr']=e7
    
    
 
    payload = json.dumps(e2)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)