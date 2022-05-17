import json
import requests
from static import *

url = "https://arl2.api.myob.com/accountright/53f60d69-ae83-4722-99a8-bdfc30d65040/Purchase/Bill/Item"

response = requests.request("GET", url, headers=headers, data=payload)

a = response.json()

arr = []
for i in range(0, len(a['Items'])):
    e = {}
    e['Supplier'] = a['Items'][i]["Supplier"]['UID']
    e['Bill_Number'] = a['Items'][i]['Number']
    e['Supplier_Invoice_Number'] = a['Items'][i]['SupplierInvoiceNumber']
    e['Date'] = a['Items'][i]['Date']
    e['Due_Date'] = a['Items'][i]['Terms']['DueDate']
    e['Total_Amount'] = a['Items'][i]['TotalAmount']

    for j in range(0, len(a['Items'][i]['Lines'])):
        e['Bill_Quantity'] = a['Items'][i]['Lines'][j]['BillQuantity']
        e['Description'] = a['Items'][i]['Lines'][j]['Description']
        e['Unit_Price'] = a['Items'][i]['Lines'][j]['UnitPrice']
        e['Tax_Code'] = a['Items'][i]['Lines'][j]['TaxCode']['Code']

    arr.append(e)


path = input("Enter a path : ")
jsonString = json.dumps(arr)
jsonFile = open("{}/bill.json".format(path), "w")
jsonFile.write(jsonString)
jsonFile.close()
