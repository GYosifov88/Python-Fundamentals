number_of_rooms = int(input())
free_chairs = 0
not_enough_room = False
for i in range (1, number_of_rooms + 1):
    current_case = input().split(' ')
    number_of_chairs = current_case[0]
    number_of_visitors = int(current_case[1])
    num_of_chairs = number_of_chairs.count('X')
    if number_of_visitors <= num_of_chairs:
        free_chairs += (num_of_chairs - number_of_visitors)
    elif number_of_visitors > num_of_chairs:
        needed_chairs_in_room = abs(number_of_visitors-num_of_chairs)
        not_enough_room = True
        print(f"{needed_chairs_in_room} more chairs needed in room {i}")

if not not_enough_room:
    print(f"Game On, {free_chairs} free chairs left")