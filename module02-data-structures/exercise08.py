ege = {"izmir": 232}
akdeniz = {"antalya": 242}
marmara = {"istanbul": {"anadolu": 216, "avrupa": 212}, "edirne": 1, "tekirdag": 2}
area_codes = {**ege, **akdeniz, **marmara}  # packing dictionaries
cities = (*ege, *akdeniz, *marmara)  # packing only keys
first, second, *remaining = area_codes
print(first)
print(second)
print(remaining)
