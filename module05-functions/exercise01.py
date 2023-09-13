"""
3n+1 problem
7  -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5
16 ->  8 ->  4 ->  2 -> (1)
14:25
"""


def fun(n):
    sequence = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


sequences = []
for n in range(2, 1_000_000):
    sequence = fun(n)
    sequences.append(sequence)
    # print(f"{n}: {len(sequence)}")

sequences.sort(key=lambda sequence: len(sequence), reverse=True)
print(f"{sequences[0][0]}: {len(sequences[0])}")
print(sequences[0])
# 837799 = 653 * 1283
