todo_list = ["" for i in range(11)]

command = input()

while command != 'End':
    task = command.split('-')
    importance = int(task[0])
    thing_to_do = task[1]
    todo_list[importance] = thing_to_do

    command = input()

final_list = [x for x in todo_list if x != ""]
print(final_list)