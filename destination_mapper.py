import re

text = input()
travel_points = 0
destination_list = list()
regex = r"([=|/])(?P<destination>[A-Z][A-Za-z]{2,})\1"

matches = re.finditer(regex, text)

for match in matches:
    destination = match.group('destination')
    destination_list.append(destination)

for k in destination_list:
    travel_points += len(k)

print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {travel_points}")
