town_list = dict()

first_command = input()

while first_command != 'Sail':
    current = first_command.split('||')
    city = current[0]
    population = int(current[1])
    gold = int(current[2])
    if city not in town_list.keys():
        town_list[city] = {'Population': population, 'Gold': gold}
    else:
        town_list[city]['Population'] += population
        town_list[city]['Gold'] += gold

    first_command = input()

second_command = input()

while second_command != 'End':
    events = second_command.split('=>')
    action = events[0]
    town = events[1]
    if action == 'Plunder':
        people = int(events[2])
        gold_amount = int(events[3])
        town_list[town]['Population'] -= people
        town_list[town]['Gold'] -= gold_amount
        print(f"{town} plundered! {gold_amount} gold stolen, {people} citizens killed.")
        if town_list[town]['Population'] == 0 or town_list[town]['Gold'] == 0:
            del town_list[town]
            print(f"{town} has been wiped off the map!")

    if action == 'Prosper':
        add_gold = int(events[2])
        if add_gold >= 0:
            town_list[town]['Gold'] += add_gold
            print(f"{add_gold} gold added to the city treasury. {town} now has {town_list[town]['Gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    second_command = input()

if len(town_list) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(town_list)} wealthy settlements to go to:")
    for city in town_list.keys():
        print(f"{city} -> Population: {town_list[city]['Population'] } citizens, Gold: {town_list[city]['Gold']} kg")
