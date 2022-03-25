quntity_food_kilos = float(input())
quntity_hay_kilos = float(input())
quntity_cover_kilos = float(input())
guinea_pig_weight_kilos = float(input())
month = 30
quntity_food_grams = quntity_food_kilos * 1000
quntity_hay_grams = quntity_hay_kilos * 1000
quntity_cover_grams = quntity_cover_kilos * 1000
guinea_pig_grams = guinea_pig_weight_kilos * 1000
not_enough_food = False

for i in range (1, month + 1):
    quntity_food_grams -= 300

    if i % 2 == 0:
        quntity_hay_grams -= (quntity_food_grams * 0.05)
    if i % 3 == 0:
        quntity_cover_grams -= guinea_pig_grams / 3

    if quntity_food_grams <= 0 or quntity_hay_grams <= 0 or quntity_cover_grams <= 0:
        not_enough_food = True
        print("Merry must go to the pet store!")
        break

if not not_enough_food:
    print(f"Everything is fine! Puppy is happy! Food: {quntity_food_grams/1000:.2f}, Hay: {quntity_hay_grams/1000:.2f}, Cover: {quntity_cover_grams/1000:.2f}.")
