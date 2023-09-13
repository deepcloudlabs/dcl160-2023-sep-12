numbers = [10, 20, 30, 40, None, None, None, 35, 42, None, None, 37, 34]
# external loop
total = sum([num ** 3 for num in numbers if num is not None])
print(total)  # 306920
