event = input().split('|')
initial_energy = 100
initial_coins = 100
close_condition = False
for events in event:
    current_event = events.split('-')
    event_type = current_event[0]
    event_points = int(current_event[1])

    if event_type == 'rest':
        if initial_energy >= 100:
            initial_energy = 100
            print("You gained 0 energy.")
        else:
            initial_energy += event_points
            print (f"You gained {event_points} energy.")

        print (f"Current energy: {initial_energy}.")

    elif event_type == 'order':
        if initial_energy >= 30:
            print(f"You earned {event_points} coins.")
            initial_coins += event_points
            initial_energy -= 30
        else:
            initial_energy += 50
            print ("You had to rest!")
    else:
        if initial_coins >= event_points:
            print (f"You bought {event_type}.")
            initial_coins -= event_points
        else:
            print (f"Closed! Cannot afford {event_type}.")
            close_condition = True
            break

if not close_condition:
    print ("Day completed!")
    print (f"Coins: {initial_coins}")
    print (f"Energy: {initial_energy}")