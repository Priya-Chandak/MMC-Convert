import json
from ast import Break
import json
from os import path
from os.path import exists
import requests
from static import payload, headers


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Supplier"
response = requests.request("GET", url, headers=headers, data=payload)
a = response.json()

n = a['Count']
count = 0

while n != 0:
    n //= 10
    count += 1

if count == 4:
    limit = 1000
elif count == 3:
    limit = 100
else:
    limit = 10

print("Number of digits: " + str(count))
print(limit)

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Supplier/?$top={}".format(
    limit)
response = requests.request("GET", url, headers=headers, data=payload)
a = response.json()
path = input("Enter a Path:")


def get_data(url):
    response = requests.request("GET", url, headers=headers, data=payload)
    a = response.json()

    arr = []
    for i in range(0, len(a['Items'])):
        e = {}
        if a['Items'][i]["IsIndividual"] == True:
            e['FirstName'] = a['Items'][i]["FirstName"]
            e['LastName'] = a['Items'][i]["LastName"]
            e['CompanyName'] = '--'
        else:
            e['FirstName'] = '--'
            e['LastName'] = '--'
            e['CompanyName'] = a['Items'][i]['CompanyName']

        e['ABN'] = a['Items'][i]["BuyingDetails"]['ABN']
        e['BSB'] = a['Items'][i]["PaymentDetails"]['BSBNumber']
        e['TaxIdNumber'] = a['Items'][i]["BuyingDetails"]['TaxIdNumber']
        e['Bank_Acc_no'] = a['Items'][i]["PaymentDetails"]['BankAccountNumber']
        e['Bank_Acc_Name'] = a['Items'][i]["PaymentDetails"]['BankAccountName']
        e['Statement_Text'] = a['Items'][i]["PaymentDetails"]['StatementText']

        if a['Items'][i]["BuyingDetails"]['ExpenseAccount'] != None:
            e['Expense_Account'] = a['Items'][i]["BuyingDetails"]['ExpenseAccount']['Name']
        else:
            e['Expense_Account'] = '--'

        if a['Items'][i]['Addresses'] != None:
            for j in range(0, len(a['Items'][i]['Addresses'])):
                e['city'] = a['Items'][i]["Addresses"][j]['City']
                e['Country'] = a['Items'][i]["Addresses"][j]['Country']
                e['Street'] = a['Items'][i]["Addresses"][j]['Street']
                e['State'] = a['Items'][i]["Addresses"][j]['State']
                e['PostCode'] = a['Items'][i]["Addresses"][j]['PostCode']
                e['Email'] = a['Items'][i]["Addresses"][j]['Email']
                e['Website'] = a['Items'][i]["Addresses"][j]['Website']
                e['Contact_Person'] = a['Items'][i]["Addresses"][j]['ContactName']
                e['Phone'] = a['Items'][i]["Addresses"][j]['Phone1']

        else:
            e['city'] = '--'
            e['Country'] = '--'
            e['State'] = '--'
            e['PostCode'] = '--'
            e['Email'] = '--'
            e['Website'] = '--'
            e['Contact_Person'] = '--'
            e['Phone1'] = '--'

        arr.append(e)

        filename = "{}/supplier.json".format(path)
        file_exists = exists("{}/supplier.json".format(path))

        if file_exists == False:
            with open("{}/supplier.json".format(path), "w") as jsonFile:
                jsonString = json.dumps(arr)
                jsonFile.write(jsonString)
                jsonFile.close()
            print("The json file is created")
        else:
            with open(filename) as fp:
                listObj = json.load(fp)
                listObj.append(e)
                with open(filename, 'w') as json_file:
                    json.dump(listObj, json_file, separators=(',', ': '))

    if a['NextPageLink'] != None:
        print(a['NextPageLink'])
        get_data(a['NextPageLink'])

    else:
        print("Data Over")
        Break


get_data(url)
