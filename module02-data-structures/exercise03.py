odds = (1, 3, 5, 7, 9)  # immutable
evens = (2, 4, 6, 8, 10)
numbers = (odds, evens)
print(len(odds))
print(len(evens))
print(len(numbers))
print(numbers[0][2])  # 5
print(numbers[1][-2])  # 8
packed_numbers = (*odds, *evens)  # packing
print(len(packed_numbers))
print(packed_numbers[0])  # 1
print(packed_numbers[-1])  # 10
sorted_numbers = sorted(packed_numbers, reverse=True)
print(packed_numbers)
print(sorted_numbers)
print(type(sorted_numbers))
