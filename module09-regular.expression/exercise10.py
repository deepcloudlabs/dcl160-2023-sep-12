"""
words that do NOT have any char from i, u, o, a, e
"""
import re

pattern = "[^iaeo]*"

with open("dictionary-tur.txt", "rt") as tur_dic:
    for word in tur_dic.readlines():
        if re.fullmatch(pattern, word.strip()):
            print(word.strip())
