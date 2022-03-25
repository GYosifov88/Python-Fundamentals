def order_cost (type, quantity):
    if type == 'coffee':
        return quantity * 1.50
    elif type == 'coke':
        return quantity * 1.40
    elif type == 'water':
        return quantity * 1.00
    elif type == 'snacks':
        return quantity * 2.00

current_type = input()
current_quantity = int(input())
final_price = (order_cost(current_type, current_quantity))

print(f'{final_price:.2f}')