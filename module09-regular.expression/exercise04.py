import re
"""
    \d -> digit: [0-9]
    \D -> not digit: [^0-9]
    \w -> [a-z]
    \W -> [^a-z]
    \s -> [ \n\t\r]
    \S -> [^ \n\t\r]
"""
identities = [
    "12345678910",
    "1234568910",
    "123456789101",
    "1234567a910",
    "1234567_910"
]
for identity in identities:
    if not re.fullmatch("\d{11}", identity):
        print(identity)
