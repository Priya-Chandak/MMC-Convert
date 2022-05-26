from math import expm1
import requests
import json
from static import headers
path = input("path :")

with open('{}/employee.json'.format(path), 'r') as f:
    data = json.load(f)

e1=[]
for i in range(0,len(data)):
    e=data[i]
    e1.append(e)


url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/employee?minorversion=14"

for i in range(0, len(e1)):
    e2 = {}
    e3 = {}
    e4 = {}
    e2['SSN'] = e1[i]['Employee_ID_Number']
    e2['GivenName'] = e1[i]['FirstName']
    e2['FamilyName'] = e1[i]['LastName']
    e3['Id'] = '1'
    e3['Line1'] = e1[i]['Addresses'][0]['Street']
    e3['City'] = e1[i]['Addresses'][0]['City']
    e3['CountrySubDivisionCode'] = e1[i]['Addresses'][0]['State']
    e3['PostalCode'] = e1[i]['Addresses'][0]['PostCode']
    e4['FreeFormNumber'] = e1[i]['Addresses'][0]['Phone1']
    e2['PrimaryAddr'] = e3
    e2['PrimaryPhone'] = e4

    payload = json.dumps(e2)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    print(response)
    
