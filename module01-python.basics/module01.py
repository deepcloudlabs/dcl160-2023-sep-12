import this

number = 42
type(number)

number = "kate austen"
type(number)

pi = 3.1415161718
type(pi)

salary = None
type(salary)

rate = 3 // 2
print(rate)
type(rate)

rate = float('NaN')
print(rate)

import math

rate1 = math.nan
rate2 = math.nan

print(rate1 != rate1)

print(math.isnan(rate1))

rate3 = float('inf')
print(rate3)
print(type(rate3))

math.isinf(rate3)

rate4 = 42.108
math.isfinite(rate4)

money = 2.0 - 1.1
money == 0.9

money = 100 * 4.35
money == 435

rate5 = ( 0.1 + 0.2 ) + 0.3
rate6 = 0.1 + (0.2 + 0.3)

print(rate5 == rate6)

val = 2 ** 10000
val

num = 3615 % 2 == 0
print(num)

num1 = ( 3 + 4 ) * 5
print(num1)

from mpmath import *

mp.dps = 100000
mp.pretty = True

pi2 = 4 * atan(1)

fullname = "KAte AUSten"
print(fullname)
print(len(fullname))

type(fullname)

fullname.lower()

fullname.upper()

str1 = "\u20ba"
print(str1)

str2 = b"\xf0\x9d\x84\x9e"
print(str2.decode("utf-8"))
print(type(str2))

len(str2)

len(str2.decode("utf-8"))

print("hello", "world","mars","jupiter")

i = 42
j = 108
print("%x:%o" % (i,j))

print("%.3f" % (pi2))

print(f"{i}:{j}")

lines = "this is the first line.\nthis is the second line.\n\tthis is the third line."
print(lines)

movies = "<movies>\n\t<movie>\n\t\t<title>A Movie Title</title>\n\t</movie>\n</movies>"
print(movies)

movies2 = """<movies>
  <movie>
    <title>A Movie Title</title>
  </movie>
</movies>
"""
print(movies2)

movies2

c1 = complex(1,2)
print(c1.real,"+j ",c1.imag)

type(c1)

print(c1.conjugate())

(c1 * c1.conjugate()).real

str2 = 'Jack\'s House'
print(str2)

multi_line = """Jack's
House
Address: "Kuyu Sokak"
"""
print(multi_line)
