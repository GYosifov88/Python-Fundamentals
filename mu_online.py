dungeon_rooms = input().split('|')
initial_health = 100
bitcoins = 0
success = True
number_of_rooms = 0
for event in dungeon_rooms:
    current_event = event.split(' ')
    event_type = current_event[0]
    points = int(current_event[1])
    number_of_rooms += 1
    if event_type == 'potion':
        if initial_health >= 100:
            initial_health = 100
            print ("You healed for 0 hp.")
        else:
            initial_health += points
            if initial_health >= 100:
                current_gained_points = 100 - (initial_health - points)
                initial_health = 100
                print (f"You healed for {current_gained_points} hp.")
            else:
                print(f"You healed for {points} hp.")
        print(f"Current health: {initial_health} hp.")

    elif event_type == 'chest':
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        initial_health -= points
        if initial_health > 0:
            print(f"You slayed {event_type}.")
        else:
            print(f"You died! Killed by {event_type}." )
            print(f"Best room: {number_of_rooms}")
            success = False
            break
if success:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")
