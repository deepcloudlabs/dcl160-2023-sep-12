numbers = [10, 20, 30, 40, None, None, None, 35, 42, None, None, 37, 34]
while numbers.count(None) > 0:  # external loop
    numbers.remove(None)
print(numbers)
