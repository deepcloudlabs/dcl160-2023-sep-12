import json

with open("employees.json", mode="rt") as myfile:
    employees = json.load(myfile)
    for employee in employees:
        print(employee)
