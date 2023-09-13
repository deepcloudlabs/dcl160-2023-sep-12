city1 = "istanbul"
city2 = "istanbul"
city3 = "istanbul"
print(city1[0])
# object pooling/caching
# city1[0] = "İ" # immutable
city1 = "ankara"
print(city1)
print(city2)
print(city3)
capitalizedCity1 = city1.upper()
print(city1)
print(capitalizedCity1)
