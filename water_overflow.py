number_of_lines = int(input())
capacity = 255
poured_water = 0
left_water = 0
is_tank_full = False

for i in range (number_of_lines):
    litres = int(input())
    if litres > 255:
        print("Insufficient capacity!")
        continue
    if litres > capacity:
        print("Insufficient capacity!")
        continue

    poured_water += litres
    capacity -= litres

print(poured_water)
