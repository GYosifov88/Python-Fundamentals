experience_amount = float(input())
count_of_battles = int(input())
needed_experience = 0
number_of_battles = 0
is_experience_gained = False
for battle in range (1, count_of_battles +1):
    experience_gained_per_battle = float(input())
    number_of_battles += 1
    if battle % 3 == 0:
        experience_gained_per_battle += experience_gained_per_battle * 0.15
        needed_experience += experience_gained_per_battle
    elif battle % 5 == 0:
        experience_gained_per_battle -= experience_gained_per_battle * 0.10
        needed_experience += experience_gained_per_battle
    elif battle % 15 == 0:
        experience_gained_per_battle += experience_gained_per_battle * 0.05
        needed_experience += experience_gained_per_battle
    else:
        needed_experience += experience_gained_per_battle

    if needed_experience >= experience_amount:
        print(f'Player successfully collected his needed experience for {number_of_battles} battles.')
        break
if needed_experience < experience_amount:
    insufficient_experience = experience_amount - needed_experience
    print(f'Player was not able to collect the needed experience, {insufficient_experience:.2f} more needed.')


