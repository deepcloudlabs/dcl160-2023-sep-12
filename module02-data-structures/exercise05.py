area_codes = {"izmir": 232, "istanbul": {"anadolu": 216, "avrupa": 212}, "ankara": 312}
print(f'Area Code for "Ankara" is {area_codes["ankara"]}')
print(f'Area Code for "istanbul avrupa" is {area_codes["istanbul"]["avrupa"]}')
area_codes["antalya"] = 242
print(f"Keys  : {area_codes.keys()}")
print(f"Values: {area_codes.values()}")
