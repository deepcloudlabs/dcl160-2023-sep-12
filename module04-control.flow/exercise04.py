numbers = [10, 20, 30, 40, None, None, None, 35, 42, None, None, 37, 34]
values = []
for num in numbers:
    if num is not None:
        values.append(num)
print(values)
