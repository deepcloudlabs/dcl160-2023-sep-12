def gun(x=10, y=20, z=30):
    return x + y * z


# print(f"gun(10,20,30): {gun(10, 20, 30)}")  # 610
#print(f"gun(): {gun(10,20, 30)}")  # TypeError: gun() missing 1 required positional argument: 'z'

print(f"gun(): {gun()}")  # 610
print(f"gun(1000): {gun(1_000)}")  # 1600
print(f"gun(100,200): {gun(100,200)}")  # 6100
print(f"gun(100,200,300): {gun(100,200,300)}")  # 60100
