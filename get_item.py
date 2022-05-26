import json
from ast import Break
import json
from os import path
from os.path import exists
import requests
from static import payload, headers


url = "https://api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Inventory/Item"
response = requests.request("GET", url, headers=headers, data=payload)
a = response.json()

n = a['Count']
count = 0

while n != 0:
    n //= 10
    count += 1

if count >= 4:
    limit = 1000
elif count == 3:
    limit = 100
else:
    limit = 10

print("Number of digits: " + str(count))
print(limit)

url = "https://api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Inventory/Item/?$top={}".format(
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
        e['UID'] = a['Items'][i]['UID']
        e['Description'] = a['Items'][i]['Description']
        e['Number'] = a['Items'][i]['Number']
        e['Name'] = a['Items'][i]['Name']
        e['ExpenseAccount'] = a['Items'][i]['ExpenseAccount']
        e['Income_Account_ID'] = a['Items'][i]['IncomeAccount']['UID']
        e['Income_Account_Name'] = a['Items'][i]['IncomeAccount']['Name']
        e['Is_Tax_Inclusive'] = a['Items'][i]['SellingDetails']['IsTaxInclusive']
        
        if a['Items'][i]['AssetAccount'] != None:
            e['Asset_Account_ID'] = a['Items'][i]['AssetAccount']['UID']
            e['Asset_Account_Name'] = a['Items'][i]['AssetAccount']['Name']
        else:
            pass
        
        if a['Items'][i]['CostOfSalesAccount'] != None:
            e['Expense_Account_ID'] = a['Items'][i]['CostOfSalesAccount']['UID']
            e['Expense_Account_Name'] = a['Items'][i]['CostOfSalesAccount']['Name']


        arr.append(e)

        filename = "{}/item.json".format(path)
        file_exists = exists("{}/item.json".format(path))

        if file_exists == False:
            with open("{}/item.json".format(path), "w") as jsonFile:
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

