text = input().split(" ")
dictionary = dict()

for i in range (0, len(text), 2):
    key = text[i]
    value = text[i + 1]
    dictionary[key] = int(value)
print(dictionary)
