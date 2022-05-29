import requests
import json
path = input("path :")

with open('{}/QBO_Employee.json'.format(path), 'r') as f:
    data = json.load(f)

QuerySet = data['QueryResponse']['Employee']

employee_id = []
for i in range(0, len(QuerySet)):
    QuerySet1 = {}
    QuerySet1['ID'] = QuerySet[i]['Id']
    QuerySet1['Name'] = QuerySet[i]['DisplayName']
    employee_id.append(QuerySet1)

print(employee_id)


"""
Available Employees : 
['63', '55', '69', '72', '66', '54', '58', '59', '60', '67', '62', '70',
 '64', '71', '65', '73', '76', '75', '74', '61']

"""
