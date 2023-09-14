import csv

with open("employees.csv", mode="rt") as myfile:
    employees = csv.reader(myfile)
    # writer.writerows(employees)
    for employee in employees:
        print(employee)