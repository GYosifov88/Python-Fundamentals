text = input()
text = text.replace(' ', "")
dictionary = dict()
for x in text:
    if x not in dictionary:
        dictionary[x] = 1
    else:
        dictionary[x] += 1

for char in dictionary.keys():
    print(f"{char} -> {dictionary[char]}")
    