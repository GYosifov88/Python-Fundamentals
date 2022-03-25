import re

text = input()
food_list = list()
total_calories = 0
regex = r"([#|\|])(?P<food>([A-Za-z\s])+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]{0,10000})\1"

matches = re.finditer(regex, text)

for match in matches:
    food = match.group('food')
    date = match.group('date')
    calories = match.group('calories')
    food_list.append(food)
    food_list.append(date)
    food_list.append(calories)
    total_calories += int(calories)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for item, date, cal in zip(food_list[0::3], food_list[1::3], food_list[2::3]):

    print(f"Item: {item}, Best before: {date}, Nutrition: {cal}")
