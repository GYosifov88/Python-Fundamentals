number_of_orders = int(input())
total_cost = 0
for orders in range (number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    cost = price_per_capsule * days * capsules_count
    print (f"The price for the coffee is: ${cost:.2f}")
    total_cost +=cost

print (f"Total: ${total_cost:.2f}")