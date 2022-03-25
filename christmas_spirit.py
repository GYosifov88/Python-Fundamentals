quantity= int(input())
days_left = int(input())

ornament = 2
skirt = 5
garlands = 3
lights = 15

cost = 0
spirit = 0
last_day = 0
for x in range (1, days_left + 1):
    if x % 11 == 0:
        quantity +=2
    if x % 2 == 0:
        spirit +=5
        cost += quantity * ornament
    if x % 3 == 0:
        spirit += 13
        cost += quantity * skirt + quantity * garlands
    if x % 5 == 0:
        spirit += 17
        cost += lights * quantity
    if x % 5 == 0 and x % 3 == 0:
        spirit +=30
    if x % 10 == 0:
        spirit -= 20
        cost += lights + skirt + garlands

    last_day = x

if last_day % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")

