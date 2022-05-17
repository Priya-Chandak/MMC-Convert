import json
import requests
from static import *


url1 = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Employee"


response1 = requests.request("GET", url1, headers=headers, data=payload)
a = response1.json()

url2 = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Payroll/Timesheet"
response2 = requests.request("GET", url2, headers=headers, data=payload)

z = response2.json()


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


path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/employee.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
