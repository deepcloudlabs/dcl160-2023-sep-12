def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def fun(n):
    sequence = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence
