cities_list = dict()
command = input()

while command != 'Sail':
    current_event = command.split('||')
    city_name = current_event[0]
    population = int(current_event[1])
    gold = int(current_event[2])
    if city_name not in cities_list.keys():
        cities_list[city_name] = {'Population': population, 'Gold': gold}
    else:
        cities_list[city_name]['Population'] += population
        cities_list[city_name]['Gold'] += gold
    command = input()


second_command = input()

while second_command != 'End':
    current_action = second_command.split('=>')
    event = current_action[0]
    town = current_action[1]

    if event == 'Plunder':
        people = int(current_action[2])
        loot_gold = int(current_action[3])
        cities_list[town]['Population'] -= people
        cities_list[town]['Gold'] -= loot_gold
        print(f"{town} plundered! {loot_gold} gold stolen, {people} citizens killed.")
        if cities_list[town]['Population'] <= 0 or cities_list[town]['Gold'] <= 0:
            del cities_list[town]
            print(f"{town} has been wiped off the map!")

    if event == 'Prosper':
        gained_gold = int(current_action[2])
        if gained_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_list[town]['Gold'] += gained_gold
            print(f"{gained_gold} gold added to the city treasury. {town} now has {cities_list[town]['Gold']} gold.")

    second_command = input()

if len(cities_list) > 0:
    print(f"Ahoy, Captain! There are {len(cities_list)} wealthy settlements to go to:")
    for city in cities_list.keys():
        print(f"{city} -> Population: {cities_list[city]['Population']} citizens, Gold: {cities_list[city]['Gold'] } kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")