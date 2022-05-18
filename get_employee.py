import json
from ast import Break
import json
from os import path
from os.path import exists
import requests
from static import payload, headers


url1 = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Employee"
response1 = requests.request("GET", url1, headers=headers, data=payload)
a = response1.json()

url2 = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Payroll/Timesheet"
response2 = requests.request("GET", url2, headers=headers, data=payload)
z = response2.json()


n1 = a['Count']
count1 = 0

while n1 != 0:
    n1 //= 10
    count1 += 1

if count1 == 4:
    limit1 = 1000
elif count1 == 3:
    limit1 = 100
else:
    limit1 = 10

    
n2 = z['Count']
count2 = 0

while n2 != 0:
    n2 //= 10
    count2 += 1

if count2 == 4:
    limit2 = 1000
elif count2 == 3:
    limit2 = 100
else:
    limit2 = 10

url1 = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Employee/?$top={}".format(
    limit1)
response = requests.request("GET", url1, headers=headers, data=payload)
a = response.json()

url2 = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Payroll/Timesheet/?$top={}".format(
    limit2)
response2 = requests.request("GET", url2, headers=headers, data=payload)
z = response2.json()


path=input("Enter a Path:")
    

def get_data(url):
    response = requests.request("GET", url, headers=headers, data=payload)
    a = response.json()

    arr = []
    for i in range(0, len(a['Items'])):
        e = {}

        e['Employee_ID'] = a['Items'][i]["DisplayID"]
        e['Employee_ID_Number'] = a['Items'][i]["UID"]
        e['Start_Date'] = z['Items'][i]['StartDate']
        e['End_Date'] = z['Items'][i]['EndDate']

        if a['Items'][i]["IsIndividual"] == True:
            e['FirstName'] = a['Items'][i]["FirstName"]
            e['LastName'] = a['Items'][i]["LastName"]
            e["Company_Name"] = "--"
        else:
            e["Company_Name"] = a['Items'][i]["CompanyName"]
            e['FirstName'] = "--"
            e['LastName'] = "--"

        if "TimeBillingDetails" in a["Items"][i]:
            if not a['Items'][i]["TimeBillingDetails"]:
                e['Cost_Per_Hour'] = "--"
            else:
                e['Cost_Per_Hour'] = a['Items'][i]["TimeBillingDetails"]["CostPerHour"]

        if "Addresses" in a["Items"][i]:
            if not a['Items'][i]["Addresses"]:
                e['Addresses'] = "--"
            else:
                e['Addresses'] = a['Items'][i]["Addresses"]

        arr.append(e)

        filename = "{}/employee.json".format(path)
        file_exists = exists("{}/employee.json".format(path))

        if file_exists == False:
            with open("{}/employee.json".format(path), "w") as jsonFile:
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


