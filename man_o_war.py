pirate_ship_initial_status_list = input().split('>')
pirate_ship_initial_status = list(map(int, pirate_ship_initial_status_list))
warship_ship_initial_status_list = input().split('>')
warship_ship_initial_status = list(map(int, warship_ship_initial_status_list))
maximum_health = int(input())
warship_sunk = False
pirate_ship_sunk = False

command = input()

while command != 'Retire':
    current_command = command.split(' ')
    action = current_command[0]

    if action == 'Fire':
        section_index = int(current_command[1])
        damage = int(current_command[2])
        if section_index in range (len(warship_ship_initial_status)):
            warship_ship_initial_status[section_index] -= damage
            if int(warship_ship_initial_status[section_index]) <= 0:
                print("You won! The enemy ship has sunken.")
                warship_sunk = True
                break
    if action == 'Defend':
        starting_index = int(current_command[1])
        last_index = int(current_command[2])
        damage = int(current_command[3])
        if starting_index in range (len(pirate_ship_initial_status)) and last_index in range (len(pirate_ship_initial_status)):
            for k in range (starting_index, last_index + 1):
                pirate_ship_initial_status[k] -= damage
                if int(pirate_ship_initial_status[k]) <= 0:
                    print("You lost! The pirate ship has sunken.")
                    pirate_ship_sunk = True
                    break
    if action == 'Repair':
        index_to_repair = int(current_command[1])
        health = int(current_command[2])
        if index_to_repair in range (len(pirate_ship_initial_status)):
            pirate_ship_initial_status[index_to_repair] += health
            if int(pirate_ship_initial_status[index_to_repair]) >= maximum_health:
                pirate_ship_initial_status[index_to_repair] = maximum_health

    if action == 'Status':
        counter_repair = 0
        for i in pirate_ship_initial_status:
            if i < maximum_health * 0.2:
                counter_repair += 1
        print(f"{counter_repair} sections need repair.")

    command = input()

if warship_sunk == False and pirate_ship_sunk == False:
    sum_pirate = sum(pirate_ship_initial_status)
    sum_warship = sum(warship_ship_initial_status)
    print(f"Pirate ship status: {sum_pirate}")
    print(f"Warship status: {sum_warship}")
