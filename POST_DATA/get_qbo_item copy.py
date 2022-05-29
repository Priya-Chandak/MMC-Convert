import requests
import json
from static import headers

path = input("Enter a path to store the file :  ")

import requests

url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/query?minorversion=14"

payload = "select * from item startposition 1 maxresults 25"

response = requests.request("POST", url, headers=headers, data=payload)

JsonResponse = response.json()

with open("{}/QBO_Item.json".format(path), "w") as jsonFile:
    jsonString = json.dumps(JsonResponse)
    jsonFile.write(jsonString)
    jsonFile.close()
print("The json file is created")

