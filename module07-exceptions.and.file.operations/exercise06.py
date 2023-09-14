import pickle

with open("employees.pkl", mode="rb") as myfile:
    employees = pickle.load(myfile)
    for employee in employees:
        print(employee)
