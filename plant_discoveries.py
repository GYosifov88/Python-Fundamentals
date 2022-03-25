number = int(input())
plants = {}
for num in range(number):
    new_plant = input().split('<->')
    plant = new_plant[0]
    rarity = int(new_plant[1])
    if plant in plants.keys():
        plants[plant]['Rarity'] += rarity
        plants[plant]['Rating'] = []
    else:
        plants[plant] = {'Rarity': rarity, 'Rating': []}


command = input()

while command != "Exhibition":
    current_command = command.split(': ')
    action = current_command[0]

    if action == 'Rate':
        current_plant_action = current_command[1].split(' - ')
        add_plant = current_plant_action[0]
        rating = int(current_plant_action[1])
        if add_plant in plants.keys():
            plants[add_plant]['Rating'].append(rating)
        else:
            print('error')

    elif action == 'Update':
        current_plant_action = current_command[1].split(' - ')
        add_plant = current_plant_action[0]
        new_rarity = int(current_plant_action[1])
        if add_plant in plants.keys():
            plants[add_plant]['Rarity'] = new_rarity
        else:
            print('error')

    elif action == 'Reset':
        current_plant_action = current_command[1].split(' - ')
        reset_plant = current_plant_action[0]
        if reset_plant in plants.keys():
            plants[reset_plant]['Rating'] = []
        else:
            print('error')

    command = input()


for j, k in plants.items():
    if not plants[j]['Rating']:
        plants[j]['Rating'] = 0
    else:
        plants[j]['Rating'] = sum(plants[j]['Rating']) / len(plants[j]['Rating'])

print("Plants for the exhibition:")
for name in plants:
    print(f"- {name}; Rarity: {plants[name]['Rarity']}; Rating: {plants[name]['Rating']:.2f}")
