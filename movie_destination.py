budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
day_cost = 0
if destination == 'Dubai':
    if season == 'Winter':
        day_cost = 45000
    elif season == 'Summer':
        day_cost = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        day_cost = 17000
    elif season == 'Summer':
        day_cost = 12500
elif destination == 'London':
    if season == 'Winter':
        day_cost = 24000
    elif season == 'Summer':
        day_cost = 20250

total_cost = day_cost * number_of_days

if destination == 'Dubai':
    total_cost = total_cost - (total_cost *  0.3)

if destination == 'Sofia':
    total_cost = total_cost + (total_cost * 25 / 100)

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f'The budget for the movie is enough! We have {difference:.2f} leva left!')
else:
    print (f'The director needs {difference:.2f} leva more!')