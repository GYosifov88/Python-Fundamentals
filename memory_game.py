elements = input().split(' ')
number_of_moves = 0
game_done = False

command = input()

while command != 'end':
    if command == 'end':
        break
    current_command = command.split(' ')
    first_index = int(current_command[0])
    second_index = int(current_command[1])
    if first_index == second_index or first_index not in range(len(elements)) or second_index not in range(len(elements)):
        number_of_moves += 1
        item_to_add = "-" + str(number_of_moves) + 'a'
        elements = elements[:len(elements)//2] + [item_to_add] + [item_to_add] + elements[len(elements)//2:]
        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        number_of_moves += 1
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        indexes_to_remove = [first_index, second_index]
        elements = [i for j, i in enumerate(elements) if j not in indexes_to_remove]


    elif elements[first_index] != elements[second_index]:
        number_of_moves += 1
        print("Try again!")

    if len(elements) == 0:
        game_done = True
        print(f"You have won in {number_of_moves} turns!")
        break


    command = input()


if not game_done:
    print ("Sorry you lose :(")
    print(' '.join(elements))