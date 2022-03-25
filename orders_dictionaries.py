store = dict()

command = input()

while command != 'buy':
    data = command.split(' ')
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if product not in store:
        store[product] = [price, quantity]
    else:
        store[product] = [price, (quantity + store[product][1])]


    command = input()

for key in store:
    total = store[key][0] * store[key][1]
    print (f"{key} -> {total:.2f}")
