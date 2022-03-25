number_of_people = int(input())
current_state_of_lift = input().split(' ')
new_list = []
lift_status = list(map(int, current_state_of_lift))

for wagon in lift_status:
    if wagon == 0:
        if number_of_people < 4:
            people_entering = number_of_people
            new_list.append(people_entering)
            number_of_people -= people_entering
        else:
            people_entering = 4
            new_list.append(people_entering)
            number_of_people -= people_entering
    elif wagon > 0:
        people_entering = 4 - wagon
        if people_entering <= number_of_people:
            new_list.append(4)
            number_of_people -= people_entering
        else:
            people_entering = number_of_people
            new_list.append(people_entering + wagon)
            number_of_people -= people_entering

if number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
    print(*new_list, sep=' ')

if number_of_people ==0 and new_list.count(4) != len(new_list):
    print("The lift has empty spots!")
    print(*new_list, sep=' ')

if number_of_people == 0 and new_list.count(4) == len(new_list):
    print(*new_list, sep=' ')