"""
Leap Year test
11:45
2100 not Leap Year
2200 not Leap Year
2300 not Leap Year
2400 Leap Year
2004 Leap Year
"""
year = int(input("Enter a year: "))
if not year % 4 == 0:
    print(f"{year} is NOT a leap year.")
elif not year % 100 == 0:
    print(f"{year} is a leap year.")
elif not year % 400 == 0:
    print(f"{year} is a NOT leap year.")
else:
    print(f"{year} is a leap year.")