import sys

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
complex(3, 5)

help(numbers)

for bi_module in dir(__builtins__):
    print(bi_module)

for pth in sys.path:
    print(pth)
x = 42
print(isinstance(numbers, list))
print(isinstance(x, int))
