import re

text = input()
food_list = []
total_calories = 0
regex = r"([\#|\|])([A-Za-z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]+)\1"

matches = re.findall(regex, text)

for match in matches:
    current_item = [el for el in match if el != '']
    food_list.append(current_item)
    total_calories += int(current_item[3])

days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")

for data in food_list:
    item = data[1]
    date = data[2]
    cal = data[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {cal}")


