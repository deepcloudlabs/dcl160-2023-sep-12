full_name = "kate austen"
print(len(full_name))
print(full_name)
s1 = "\u20ba"
print(s1)
encoded_s1 = s1.encode("utf-8")
print(type(encoded_s1))  # bytes
print(encoded_s1)
decoded_s1 = encoded_s1.decode("utf-8")
print(type(decoded_s1))  # str
print(decoded_s1)
