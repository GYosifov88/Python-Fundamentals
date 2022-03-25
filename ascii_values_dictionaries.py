text = input().split(', ')
# dictionary = dict()

dictionary = {x: ord(x) for x in text}

# for i in text:
#     dictionary[i] = ord(i)

print(dictionary)