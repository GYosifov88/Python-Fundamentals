shopping_list = input().split('!')
new_list = []

command = input()
while command != "Go Shopping!":
    task = command.split(' ')
    current_command = task[0]

    if current_command == 'Urgent':
        current_grocery = task[1]
        if current_grocery not in shopping_list:
            shopping_list.insert(0, current_grocery)

    if current_command == 'Unnecessary':
        current_grocery = task[1]
        if current_grocery in shopping_list:
            shopping_list.pop(shopping_list.index(current_grocery))

    if current_command == 'Correct':
        current_grocery = task[1]
        new_grocery = task[2]
        if current_grocery in shopping_list:
            shopping_list = [x.replace(current_grocery, new_grocery) for x in shopping_list]

    if current_command == 'Rearrange':
        current_grocery = task[1]
        if current_grocery in shopping_list:
            shopping_list.pop(shopping_list.index(current_grocery))
            shopping_list.append(current_grocery)

    command = input()

    if command == "Go Shopping!":
        print(', '.join(shopping_list))