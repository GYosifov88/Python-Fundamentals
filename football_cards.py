commands = input().split(" ")
my_list = []
team_a_count = 11
team_b_count = 11
condition = False
for i in commands:
    if i not in my_list:
        my_list.append(i)
        if "A" in i:
            team_a_count -= 1
        if "B" in i:
            team_b_count -= 1
        if team_a_count < 7 or team_b_count < 7:
            condition = True
            break

print(f'Team A - {team_a_count}; Team B - {team_b_count}')

if condition:
    print ("Game was terminated")