command = input()
total_price = 0
total_price_wiht_taxes = 0
total_taxes = 0
while command != "special" and command != "regular":
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print ("Invalid price!")
    else:
        tax = price * 0.2
        total_taxes += tax
        total_price += price

    command = input()

total_price_wiht_taxes = total_price + total_taxes

if command == "special":
    total_price_wiht_taxes = total_price_wiht_taxes - (total_price_wiht_taxes * 0.1)

if total_price_wiht_taxes == 0:
    print("Invalid order!" )
else:
    print("Congratulations you've just bought a new computer!")
    print (f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {total_taxes:.2f}$')
    print('-----------')
    print(f"Total price: {total_price_wiht_taxes:.2f}$")
