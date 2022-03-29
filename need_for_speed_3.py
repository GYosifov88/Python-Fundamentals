number_of_cars = int(input())
car_list = dict()
for i in range(number_of_cars):
    entry = input().split('|')
    car = entry[0]
    mileage = int(entry[1])
    fuel = int(entry[2])
    car_list[car] = {'Mileage': mileage, 'Fuel': fuel}

command = input()

while command != 'Stop':
    current_command = command.split(' : ')
    action = current_command[0]
    current_car = current_command[1]

    if action == 'Drive':
        distance = int(current_command[2])
        needed_fuel = int(current_command[3])
        if car_list[current_car]['Fuel'] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            car_list[current_car]['Fuel'] -= needed_fuel
            car_list[current_car]['Mileage'] += distance
            print(f"{current_car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if car_list[current_car]['Mileage'] >= 100000:
                del car_list[current_car]
                print(f"Time to sell the {current_car}!")

    elif action == 'Refuel':
        new_fuel = int(current_command[2])
        if car_list[current_car]['Fuel'] + new_fuel > 75:
            print(f"{current_car} refueled with {75 - car_list[current_car]['Fuel']} liters")
            car_list[current_car]['Fuel'] = 75
        else:
            car_list[current_car]['Fuel'] += new_fuel
            print(f"{current_car} refueled with {new_fuel} liters")

    elif action == 'Revert':
        kilometers = int(current_command[2])
        if (car_list[current_car]['Mileage'] - kilometers) < 10000:
            car_list[current_car]['Mileage'] = 10000
        else:
            car_list[current_car]['Mileage'] -= kilometers
            print(f"{current_car} mileage decreased by {kilometers} kilometers")

    command = input()

for car in car_list:
    print(f"{car} -> Mileage: {car_list[car]['Mileage']} kms, Fuel in the tank: {car_list[car]['Fuel']} lt.")

