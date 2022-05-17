# import json
# import requests
# from static import *


# url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Customer"

# response = requests.request("GET", url, headers=headers, data=payload)

# a = response.json()

# arr = []
# for i in range(0, len(a['Items'])):
#     e = {}
#     e['UID'] = a['Items'][i]["UID"]

#     if a['Items'][i]["IsIndividual"] == True:
#         e['FirstName'] = a['Items'][i]["FirstName"]
#         e.update({"Last_Name": a['Items'][i]["LastName"]})
#         e['LastName'] = a['Items'][i]["LastName"]

#         e.update({"Company_Name": "--"})
#     else:
#         e.update({"Company_Name": a['Items'][i]["CompanyName"]})
#         e.update({"First_Name": "--"})
#         e.update({"Last_Name": "--"})

#     if "Addresses" in a["Items"][i]:
#         if not a['Items'][i]["Addresses"]:
#             e['Addresses'] = "--"
#         else:
#             e['Addresses'] = a['Items'][i]["Addresses"]

#     arr.append(e)

# path = input("Enter a path : ")
# jsonString = json.dumps(arr)
# jsonFile = open("{}/customer.json".format(path), "w")
# jsonFile.write(jsonString)
# jsonFile.close()

from ast import Break
import pandas as pd
import json
from os import path
from os.path import exists
from static import *
import requests

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Customer/"
response = requests.request("GET", url, headers=headers, data=payload)
a=response.json()

n=a['Count']
count = 0

while n != 0:
    n //= 10
    count += 1

if count==4:
    limit = 1000
elif count==3:
    limit = 100
else:
    limit=10

print("Number of digits: " + str(count))    
print(limit)

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Contact/Customer/?$top={}".format(limit)
response = requests.request("GET", url, headers=headers, data=payload)
a=response.json()


def get_data(url):
    if a['NextPageLink'] != None:
        arr = []
        for i in range(0, len(a['Items'])):
            e = {}
            e['UID'] = a['Items'][i]["UID"]

            if a['Items'][i]["IsIndividual"] == True:
                e['FirstName'] = a['Items'][i]["FirstName"]
                e.update({"Last_Name": a['Items'][i]["LastName"]})
                e['LastName'] = a['Items'][i]["LastName"]

                e.update({"Company_Name": "--"})
            else:
                e.update({"Company_Name": a['Items'][i]["CompanyName"]})
                e.update({"First_Name": "--"})
                e.update({"Last_Name": "--"})

            if "Addresses" in a["Items"][i]:
                if not a['Items'][i]["Addresses"]:
                    e['Addresses'] = "--"
                else:
                    e['Addresses'] = a['Items'][i]["Addresses"]

            arr.append(e)
            
            filename = "C:/Users/SurajC/Downloads/Desktop/Parse_Data/Data/demo.json"
            file_exists = exists("C:/Users/SurajC/Downloads/Desktop/Parse_Data/Data/demo.json")


            if file_exists == False:
                with open("C:/Users/SurajC/Downloads/Desktop/Parse_Data/Data/demo.json", "w") as jsonFile:
                    jsonString = json.dumps(arr)
                    jsonFile.write(jsonString)
                    jsonFile.close()
                print("The json file is created")    
            else:
                with open(filename) as fp:
                    listObj = json.load(fp)
                    listObj.append(e)
                    with open(filename, 'w') as json_file:
                        json.dump(listObj, json_file,separators=(',',': '))
            get_data(a['NextPageLink'])
    else:
        Break

get_data(url)