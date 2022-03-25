dictionary = dict()

command = input()

while ':' in command:
    data = command.split(':')
    product = data[0]
    quantity = int(data[1])

    if product not in dictionary:
        dictionary[product] = quantity
    else:
        dictionary[product] += quantity

    command = input()

print("Products in stock:")
total_products = len(dictionary.keys())
total_quantity = sum(dictionary.values())

for product,quantity in dictionary.items():
    print (f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
