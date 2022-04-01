import re

participants = input().split(', ')
participants_list = dict()
digit_pattern = r'[\d]'
letter_pattern = r'[a-zA-Z]'
for k in participants:
    participants_list[k] = 0

command = input()

while command != 'end of race':
    kilometers = 0
    current_name = ''
    digit_list = list()
    letter_list = list()
    name = re.finditer(letter_pattern, command)
    meters = re.finditer(digit_pattern, command)

    for i in meters:
        digit_list.append(i.group())
    for j in digit_list:
        kilometers += int(j)
    for p in name:
        letter_list.append(p.group())
    for o in letter_list:
        current_name += o
    if current_name in participants_list:
        participants_list[current_name] += kilometers

    command = input()

my_keys = sorted(participants_list, key=participants_list.get, reverse=True)[:3]

print(f'1st place: {my_keys[0]}')
print(f'2nd place: {my_keys[1]}')
print(f'3rd place: {my_keys[2]}')
