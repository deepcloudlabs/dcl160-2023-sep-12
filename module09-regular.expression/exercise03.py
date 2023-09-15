import re
"""
  [abcd]
  [a-z]
  [02468]
  [13579]
  [0-9]
  [3-7]
  [34567]
  [a-z0-9]
  [abcdefghijklmnoprstuvyzüğşöçıABCDEFGHİJKLMNOPRSTUVYZÜĞŞÇÖ]
"""
meyveler = ["karpuz", "kavun", "KARpuz","k1raz","kIraz", "muz", "şeftali", "kivi", "elma", "armut"]
tr_letters = "abcdefghijklmnoprstuvyzüğşöçıABCDEFGHİJKLMNOPRSTUVYZÜĞŞÇÖ"
pattern1 = "^k[a-z]*z$"
pattern2 = "^[kK][a-zA-Z]*z$"
pattern3 = f"^[{tr_letters}]+$"
for meyve in meyveler:
    if re.fullmatch(pattern3, meyve):
        print(meyve)
