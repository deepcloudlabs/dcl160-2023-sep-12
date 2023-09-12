orders = [
    ("orcl", 10, 123.47, "BID"),
    ("ibm", 12000, 73.17, "ASK"),
    ("orcl", 2000, 124.38, "BID"),
    ("ibm", 20, 72.58, "ASK")
]
print(orders)
sorted_orders = sorted(orders, key = lambda order: order[2] * order[1])
print(sorted_orders)
