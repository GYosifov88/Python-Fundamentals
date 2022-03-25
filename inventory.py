journal = input().split(', ')

command = input()

while command != 'Craft!':
    current_command = command.split(' - ')
    action = current_command[0]

    if action == 'Collect':
        item = current_command[1]
        if item not in journal:
            journal.append(item)
    if action == 'Drop':
        item = current_command[1]
        if item in journal:
            journal.pop(journal.index(item))
    if action == 'Combine Items':
        item = current_command[1]
        current_switch = item.split(':')
        old_item = current_switch[0]
        new_item = current_switch[1]
        if old_item in journal:
            journal.insert(journal.index(old_item)+1, new_item)
    if action == 'Renew':
        item = current_command[1]
        if item in journal:
            journal.pop(journal.index(item))
            journal.append(item)


    command = input()
    if command == 'Craft!':
        print(', '.join(journal))