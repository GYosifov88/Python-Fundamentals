import re

command = input()
furnitures = list()
cost = 0
regex = r"^[>]{2}(?P<type>[A-Za-z]+)[<]{2}(?P<price>[0]|[1-9][0-9]*\.?[0-9]*)!(?P<quantity>[0-9]*)\b"
while command != 'Purchase':
    matches = re.finditer(regex, command)

    for match in matches:
        furnitures.append(match.group('type'))
        cost += float(match.group('price')) * int(match.group('quantity'))

    command = input()

print("Bought furniture:")

for j in furnitures:
    print(j)

print(f"Total money spend: {cost:.2f}")