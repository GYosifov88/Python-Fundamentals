products = input().split(' ')
searched_products = input().split(' ')
dictionary = dict()
for i in range (0, len(products), 2):
    product = products[i]
    value = products[i + 1]
    dictionary[product] = int(value)

for word in searched_products:
    if word in dictionary.keys():
        print(f"We have {dictionary[word]} of {word} left")
    else:
        print(f"Sorry, we don't have {word}")

