line1 = "         \n\t\t     \t\t   \tsome data.\t\t\n     more data\t    \n\n\n"
print(line1)
print("line.lstrip():")
print(line1.lstrip())
print("line.rstrip():")
print(line1.rstrip())
print("line.strip():")
print(line1.strip())
line2 = "to be or not to be"
replaced_line2 = line2.replace("to", "2")
print(f"{line2} becomes {replaced_line2}")
line3 = "11111111110,       kate austen,     tr123132354345\t,    \t\t10000000\n\t,\n1988\n"
print(line3.split(","))
for token in line3.split(","):
    print(token.strip())
