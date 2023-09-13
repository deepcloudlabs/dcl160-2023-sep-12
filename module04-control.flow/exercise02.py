user_input = input("enter an integer: ")
print(user_input)
print(type(user_input))
number = int(user_input)
print(number)
print(type(number))
"""
    if
    if / else
    if / elif
    if / elif / else
    if / elif / elif
    if / elif / elif / else
    . . . 
"""
if number < 0:
    print(f"{number} is a negative integer.")
elif number == 0:
    print(f"{number} is zero.")
else:
#elif number > 0:
    print(f"{number} is a positive integer.")
