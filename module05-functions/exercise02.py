def fun(n):  # generator function
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        print(f"fun(): {n}")
        yield n


for num in fun(837799):
    print(f"for: number= {num}")
