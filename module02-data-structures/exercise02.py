names = ("jack", "kate", "james", "sun", "jin", "ben")
print(names[0])  # the first element
print(names[1])
print(names[5])  # the last element
# print(names[6])  # raises an error: IndexError
print(names[-1])
print(names[-2])
print(len(names))
sorted_names = sorted(names, reverse=True)
print(sorted_names)

jack = ("jack shephard", "11111111110", "jack.shephard@example.com", 1982, 100_000.45)
salary = jack[-1]
print(f"salary: {salary}")
print(f"e-mail: {jack[2]}")


