"""
words longer than 12-chars in turkish dictionary
"""
import re

pattern = "???"

with open("dictionary-tur.txt", "rt") as tur_dic:
    for word in tur_dic.readlines():
        if re.fullmatch(pattern, word):
            print(word)
