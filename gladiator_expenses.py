number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_broken_times = 0
trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_armor = 0
for fights in range (1, number_of_lost_fights +1):
    if fights % 2 == 0:
        trashed_helmet += 1
    if fights % 3 == 0:
        trashed_sword += 1
    if fights % 3 == 0 and fights % 2 == 0:
        trashed_shield += 1
        shield_broken_times += 1
        if shield_broken_times % 2 == 0:
            trashed_armor += 1

expenses = (trashed_armor * armor_price) + (trashed_shield * shield_price) + (trashed_sword * sword_price) + (trashed_helmet * helmet_price)
print (f"Gladiator expenses: {expenses:.2f} aureus")


