number_of_wagons = int(input())
train = [0 for x in range(number_of_wagons)]

command = input()

while command != 'End':
    current_task = command.split(' ')
    task = current_task[0]
    if task == 'add':
        num_of_people = int(current_task[1])
        train[-1] += num_of_people

    if task == 'insert':
        wagon_index = int(current_task[1])
        num_of_people = int(current_task[2])
        train[wagon_index] += num_of_people

    if task == 'leave':
        wagon_index = int(current_task[1])
        num_of_people = int(current_task[2])
        train[wagon_index] -= num_of_people
    command = input()
print(train)


