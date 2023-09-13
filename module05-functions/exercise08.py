def en_kucuk(*values):
    min_val = values[0]
    for val in values:
        if val < min_val:
            min_val = val
    return min_val


minimum = en_kucuk(3, 47, 12, 100, 200 , 56, 23, 88, 11, 16)
print(minimum)
