import json
from ast import Break
import json
from os import path
from os.path import exists
import requests
from static import payload, headers

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/GeneralLedger/GeneralJournal"
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

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/GeneralLedger/GeneralJournal/?$top={}".format(
    limit)
response = requests.request("GET", url, headers=headers, data=payload)
a = response.json()
path = input("Enter a Path:")


def get_data(url):
    response = requests.request("GET", url, headers=headers, data=payload)
    a = response.json()

    arr = []
    for i in range(0, len(a['Items'])):
        e = {"is_credit_debit": []}
        e['Referrence_No'] = a['Items'][i]["DisplayID"]
        e['Date'] = a['Items'][i]["DateOccurred"]

        for j in range(0, len(a['Items'][i]['Lines'])):
            e['Account_Name'] = a['Items'][i]['Lines'][j]['Account']['Name']
            e["is_credit_debit"].append({"Amount": a['Items'][i]['Lines'][j]['Amount'], "IsCredit": a['Items'][i]['Lines'][j]['IsCredit'], "Description": a['Items'][i]['Lines'][j]['LineDescription']})

        arr.append(e)

        filename = "{}/journal.json".format(path)
        file_exists = exists("{}/journal.json".format(path))

        if file_exists == False:
            with open("{}/journal.json".format(path), "w") as jsonFile:
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
