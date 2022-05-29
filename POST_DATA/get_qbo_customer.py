import requests
import json
from POST_In_QBO import static
from static import headers

path = input("Enter a path to store the file :  ")

url = "https://sandbox-quickbooks.api.intuit.com/v3/company/4620816365226489730/query?minorversion=14"

payload = "Select * from Customer startposition 1 maxresults 1000"

response = requests.request("POST", url, headers=headers, data=payload)

JsonResponse = response.json()

with open("{}/QBO_Customer.json".format(path), "w") as jsonFile:
    jsonString = json.dumps(JsonResponse)
    jsonFile.write(jsonString)
    jsonFile.close()
print("The json file is created")
