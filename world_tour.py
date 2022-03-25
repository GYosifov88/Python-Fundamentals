tour_stops = input()
original_stops = tour_stops

command = input()

while command != 'Travel':
    current_action = command.split(':')
    action = current_action[0]

    if action == 'Add Stop':
        index = int(current_action[1])
        new_stop = current_action[2]
        if 0 <= index <= len(tour_stops):
            tour_stops = tour_stops[:index] + new_stop + tour_stops[index:]
            print(tour_stops)
        else:
            print(tour_stops)

    elif action == 'Remove Stop':
        start_index = int(current_action[1])
        end_index = int(current_action[2])
        if 0 <= start_index <= len(tour_stops) and 0 <= end_index <= len(tour_stops):
            tour_stops = tour_stops[0:start_index] + tour_stops[end_index+1:]
            print(tour_stops)
        else:
            print(tour_stops)

    elif action == 'Switch':
        old_string = current_action[1]
        new_string = current_action[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)
            print(tour_stops)
        else:
            print(tour_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {tour_stops}")
