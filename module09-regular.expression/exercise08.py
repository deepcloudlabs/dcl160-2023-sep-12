import re

"""
()
"""
phone = "\+\d{1,3}-\d{1,3}-\d{3}-\d{4}"
contact = "Kate Austen,Work: +90-212-555-1248,Home: +90-216-444-9854"
result = re.search(f"(\w+: {phone}),(\w+: {phone})", contact)
print(result.group())
print(result.group(1))
print(result.group(2))
