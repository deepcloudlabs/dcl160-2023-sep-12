numbers = (2, 4, 42, -3, 28, 256)
print(all(map(lambda n: n % 2 == 0, numbers)))
print(any(map(lambda n: n % 2 == 1, numbers)))
