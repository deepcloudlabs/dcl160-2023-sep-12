import re

words = []


def search_in_dictionary(pattern):
    result = []
    for word in words:
        if re.fullmatch(pattern, word.strip()):
            result.append(word.strip())
    return result
