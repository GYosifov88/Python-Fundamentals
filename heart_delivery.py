list_of_houses = input().split('@')
int_list_of_houses = list(map(int, list_of_houses))
current_position = 0
last_position = 0
command = input()
while command != 'Love!':
    task = command.split(' ')
    current_task = task[0]
    if current_task == 'Jump':
        house_index = int(task[1])
        index = house_index + current_position

        if index >= (len(int_list_of_houses)):
            index = 0

        if -1 < index < len(int_list_of_houses):
            if int_list_of_houses[index] > 0:
                int_list_of_houses[index] -= 2
                if int_list_of_houses[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")

        current_position = index
        last_position = index
    command = input()


print (f"Cupid's last position was {last_position}.")

if int_list_of_houses.count(0) == len(int_list_of_houses):
    print ("Mission was successful.")
else:
    not_celebrating_houses = len(int_list_of_houses) - int_list_of_houses.count(0)
    print (f"Cupid has failed {not_celebrating_houses} places.")
