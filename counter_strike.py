starting_energy = int(input())

energy_left = 0
won_battles = 0

command = input()

while True:
    if command == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {starting_energy}" )
        break
    distance = int(command)
    if distance > starting_energy:
        print (f"Not enough energy! Game ends with {won_battles} won battles and {starting_energy} energy")
        break
    else:
        starting_energy -= distance
        won_battles += 1
    if won_battles % 3 == 0:
        starting_energy += won_battles

    command = input()