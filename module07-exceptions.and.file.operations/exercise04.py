with open("employees.txt", mode="rt") as employees:
    for line in employees:
        full_name, department, salary, birth_year, full_time = line.split(",")
        print(f"{full_name},{department},{salary},{birth_year},{full_time}",end="")
