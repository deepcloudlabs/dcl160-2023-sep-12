import re
"""
  .
  ?
  +
  *
  {}
"""
meyveler = ["k","ka","kab","karpuz", "kavun", "kiraz", "muz", "seftali", "kivi", "elma", "armut"]
pattern1 = ".{,4}"
pattern2 = "^k.?"
for meyve in meyveler:
    if re.fullmatch(pattern2, meyve):
        print(meyve)
