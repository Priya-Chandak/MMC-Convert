import json

path1 = input("Enter a path of file-1: ")
path2 = input("Enter a path of file-2: ")


with open('{}/item_bill.json'.format(path1), 'r') as f:
    data1 = json.load(f)

with open('{}/all_bill.json'.format(path2), 'r') as f:
    data2 = json.load(f)


for i in range(0,len(data1)):
    
    if data1[i]['UID'] == data2[i]['UID']:
        data2[i].update(data1[i])
    else:
        pass

with open("{}/combined_bill.json".format(path1), "w") as jsonFile:
    jsonString = json.dumps(data2)
    jsonFile.write(jsonString)
    jsonFile.close()
print("The json file is created")