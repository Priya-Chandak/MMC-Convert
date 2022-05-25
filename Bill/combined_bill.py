import json

path1 = input("Enter a path of file: ")

with open('{}/item_bill.json'.format(path1), 'r') as f:
    data1 = json.load(f)

with open('{}/service_bill.json'.format(path1), 'r') as f:
    data2 = json.load(f)

with open('{}/professional_bill.json'.format(path1), 'r') as f:
    data3 = json.load(f)

with open('{}/misc_bill.json'.format(path1), 'r') as f:
    data4 = json.load(f)

with open('{}/all_bill.json'.format(path1), 'r') as f:
    data5 = json.load(f)

def get_data(data1):
    for i in range(0,len(data1)):
        for j in range(0,len(data5)):
            if data1[i]['UID'] == data5[j]['UID']:
                data5[j].update(data1[i])
            else:
                pass
            
    with open("{}/new.json".format(path1), "w") as jsonFile:
        jsonString = json.dumps(data5)
        jsonFile.write(jsonString)
        jsonFile.close()
    print("The json file is created")

get_data(data1)
get_data(data2)
get_data(data3)
get_data(data4)