import requests
import json
path = input("path :")

with open('{}/QBO_Customer.json'.format(path), 'r') as f:
    data = json.load(f)

e=data['QueryResponse']['Customer']

customer_id=[]
for i in range(0,len(e)):
    customer_id.append(e[i]['Id'])


"""
Available Customers : 
['80', '79', '92', '90', '1', '2', '93', '81', '82', '3', '4', '5', '6', '83', '7', '8', '9', '10', 
'11', '84', '12', '13', '14', '78', '77', '16', '85', '17', '86', 
'88', '18', '15', '91', '19', '20', '21', '22', '23', '24', '25', '87', '26', '27', '28', '29', '89']
"""