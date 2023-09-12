ege = {"izmir": 232}
akdeniz = {"antalya": 242}
marmara = {"istanbul": {"anadolu": 216, "avrupa": 212}}
area_codes = {**ege, **akdeniz, **marmara}  # packing dictionaries
cities = (*ege, *akdeniz, *marmara)  # packing only keys
print(f"cities: {cities}")
print(f'Area Code for "Antalya" is {area_codes["antalya"]}')
print(f'Area Code for "istanbul avrupa" is {area_codes["istanbul"]["avrupa"]}')
print(f"Keys  : {area_codes.keys()}")
print(f"Values: {area_codes.values()}")
print(f'is izmir in Turkey?: {"izmir" in area_codes}')
