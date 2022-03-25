initital_array = input().split(' ')
int_initial_array = list(map(int, initital_array))

command = input()

while command != 'end':
    current_command = command.split(' ')
    action = current_command[0]

    if action == 'swap':
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        int_initial_array[first_index], int_initial_array[second_index] = int_initial_array[second_index], int_initial_array[first_index]
    if action == 'multiply':
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        new_item = int_initial_array[first_index] * int_initial_array[second_index]
        int_initial_array[first_index] = new_item

    if command == 'decrease':
        int_initial_array = [i - 1 for i in int_initial_array]


    command = input()

final_list = list(map(str, int_initial_array))
print(', '.join(final_list))