"""
3n+1 problem
7  -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5
16 ->  8 ->  4 ->  2 -> (1)
14:25
"""
n = 2 ** 1000
sequence = [n]
while n > 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(n)
print(sequence)
