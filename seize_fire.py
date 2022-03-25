fires = input().split('#')
starting_water = int(input())
effort = 0
condition = False
total_fire = 0
new_list = []
type_of_fire = []
power_of_fire = []

print ('Cells:')

for current_fire in fires:
    fire = current_fire.split(' = ')
    type_of_fire = fire[0]
    power_of_fire = int(fire[1])
    condition = False

    if type_of_fire == 'High':
        if 81 <= power_of_fire <= 125:
            condition = True
    if type_of_fire == 'Medium':
        if 51 <= power_of_fire <= 80:
            condition = True
    if type_of_fire == 'Low':
        if 1 <= power_of_fire <= 50:
            condition = True


    if condition:
        if starting_water >= power_of_fire:
            starting_water -= power_of_fire
            effort += power_of_fire * 0.25
            total_fire += power_of_fire
            print(f' - {power_of_fire}')

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")