travel_route = input().split('||')
amount_of_fuel = int(input())
amount_of_ammunition = int(input())
travelled_distance = 0
for x in travel_route:
    current_command = x.split(' ')
    command = current_command[0]
    if command == 'Travel':
        value = int(current_command[1])
        if amount_of_fuel >= value:
            travelled_distance += value
            amount_of_fuel -= value
            print(f'The spaceship travelled {value} light-years.')
        else:
            print("Mission failed.")
            break
    elif command == 'Enemy':
        value = int(current_command[1])
        if amount_of_ammunition >= value:
            amount_of_ammunition -= value
            print(f'An enemy with {value} armour is defeated.')
        elif amount_of_ammunition < value:
            if amount_of_fuel >= value * 2:
                amount_of_fuel -= value * 2
                print(f'An enemy with {value} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break
    elif command == 'Repair':
        value = int(current_command[1])
        amount_of_fuel += value
        amount_of_ammunition += value * 2
        print(f'Ammunitions added: {value*2}.')
        print(f'Fuel added: {value}.')

    elif command == 'Titan':
        print('You have reached Titan, all passengers are safe.')


