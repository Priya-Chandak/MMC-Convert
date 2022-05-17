import json
from ast import Break
import json
from os import path
from os.path import exists
import requests
from static import payload, headers


url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Banking/SpendMoneyTxn"
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

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Banking/SpendMoneyTxn/?$top={}".format(
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

        e['Pay_From'] = a['Items'][i]["Account"]['Name']

        if a['Items'][i]["Contact"] != None:
            e['Pay_To'] = a['Items'][i]["Contact"]['Name']
        else:
            e['Pay_To'] = '--'

        e['Date'] = a['Items'][i]['Date']
        e['Description'] = a['Items'][i]['Memo']
        e['Is_Tax_Inclusive'] = a['Items'][i]['IsTaxInclusive']
        e['Payment_Number'] = a['Items'][i]['PaymentNumber']
        e['Amount_Paid'] = a['Items'][i]['AmountPaid']
        e['Total_Tax'] = a['Items'][i]['TotalTax']

        for j in range(0, len(a['Items'][i]['Lines'])):
            e['TaxCode_UID'] = a['Items'][i]['Lines'][j]['TaxCode']['UID']

        arr.append(e)

        filename = "{}/spend_money.json".format(path)
        file_exists = exists("{}/spend_money.json".format(path))

        if file_exists == False:
            with open("{}/spend_money.json".format(path), "w") as jsonFile:
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
