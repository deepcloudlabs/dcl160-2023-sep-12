import re

line = "1     \t\t     \t 2      3 \t     4     5     \t   "
print(re.sub("\s+", ",", line.strip()).split(","))
