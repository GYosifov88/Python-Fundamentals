heroes_number = int(input())
heroes_list = dict()

for heroes in range(heroes_number):
    hero = input().split(' ')
    hero_name = hero[0]
    hero_hit_points = int(hero[1])
    hero_mana_points = int(hero[2])
    heroes_list[hero_name] = {'HP': hero_hit_points, 'MP': hero_mana_points}


command = input()

while command != 'End':
    current_command = command.split(' - ')
    action = current_command[0]
    name_of_hero = current_command[1]

    if action == 'CastSpell':
        mp_needed = int(current_command[2])
        spell_name = current_command[3]
        if heroes_list[name_of_hero]['MP'] >= mp_needed:
            heroes_list[name_of_hero]['MP'] -= mp_needed
            print(f"{name_of_hero} has successfully cast {spell_name} and now has {heroes_list[name_of_hero]['MP']} MP!")
        else:
            print(f"{name_of_hero} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        damage = int(current_command[2])
        attacker = current_command[3]
        heroes_list[name_of_hero]['HP'] -= damage
        if heroes_list[name_of_hero]['HP'] > 0:
            print(f"{name_of_hero} was hit for {damage} HP by {attacker} and now has {heroes_list[name_of_hero]['HP']} HP left!")
        else:
            del heroes_list[name_of_hero]
            print(f"{name_of_hero} has been killed by {attacker}!")

    elif action == 'Recharge':
        amount = int(current_command[2])
        heroes_list[name_of_hero]['MP'] += amount
        if heroes_list[name_of_hero]['MP'] >= 200:
            print(f"{name_of_hero} recharged for {abs(heroes_list[name_of_hero]['MP'] - 200 - amount)} MP!")
            heroes_list[name_of_hero]['MP'] = 200
        else:
            print(f"{name_of_hero} recharged for {amount} MP!")

    elif action == 'Heal':
        heal_amount = int(current_command[2])
        heroes_list[name_of_hero]['HP'] += heal_amount
        if heroes_list[name_of_hero]['HP'] >= 100:
            print(f"{name_of_hero} healed for {abs(heroes_list[name_of_hero]['HP'] - 100 - heal_amount)} HP!")
            heroes_list[name_of_hero]['HP'] = 100
        else:
            print(f"{name_of_hero} healed for {heal_amount} HP!")

    command = input()

for hero in heroes_list:
    print(f"{hero}")
    print(f"  HP: {heroes_list[hero]['HP']}")
    print(f"  MP: {heroes_list[hero]['MP']}")

