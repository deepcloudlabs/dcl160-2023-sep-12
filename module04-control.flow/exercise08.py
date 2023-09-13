numbers = [10, 20, 30, 40, None, None, None, 35, 42, None, None, 37, 34]
total = 0
for num in numbers:  # external loop
    if num is not None:
        cubed = num ** 3
        total = total + cubed
print(total)  # 306920
