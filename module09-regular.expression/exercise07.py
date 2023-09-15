import re

"""
()
"""
contact = "Kate Austen,Home: +90-212-555-1248,Work: +90-216-444-9854"
for phone in re.finditer("\+\d{1,3}-\d{1,3}-\d{3}-\d{4}", contact):
    print(phone.group())
