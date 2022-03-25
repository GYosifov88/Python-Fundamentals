items = input().split('|')
budget = float(input())
condition = False
new_prices = []
new_prices_str = []
profit = 0
gain = 0
for current_item in items:
    item = current_item.split('->')
    type = item[0]
    price = float(item[1])
    condition = False

    if type == 'Clothes':
        if price <= 50:
            condition = True
    if type == 'Shoes':
        if price <= 35:
            condition = True
    if type == 'Accessories':
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.4
            new_price = price + (price * 0.4)
            gain += new_price
            new_prices_str.append(new_price)
            new_prices.append(f"{new_price:.2f}")


print(' '.join(new_prices))
print(f"Profit: {profit:.2f}")

amount_gained = budget + gain

if amount_gained >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")