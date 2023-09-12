employees = [
    ("jack shephard", "Sales", 100_000, 1978, True),
    ("kate austen", "IT", 200_000, 1985, False),
    ("ben linus", "Finance", 150_000, 1967, True),
    ("james sawyer", "HR", 70_000, 1979, True),
    ("kim kwon", "Sales", 120_000, 1986, True),
    ("sun kwon", "IT", 170_000, 1984, False),
    ("hugo reyes", "IT", 120_000, 1992, True)
]

sorted_employees = sorted(employees, key=lambda employee: employee[2])
print(sorted_employees)
