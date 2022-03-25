data = input()
new_data = []
strenght = 0

for char in data:
    if char.isdigit():
        strenght += int(char)
        strenght -= 1
        continue
    else:
        if strenght < 1:
            new_data.append(char)
        else:
            if char == '>':
                new_data.append(char)
            else:
                strenght -= 1
                continue
print(''.join(new_data))

