from utility.dictionary import words

print("utility module is loaded!")

with open("utility/dictionary-tur.txt", mode="rt") as tur_dic:
    print("turkish dictionary is loaded!")
    for word in tur_dic.readlines():
        words.append(word)