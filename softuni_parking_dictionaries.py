number = int(input())
parking_list = dict()

for num in range (number):
    command = input().split(' ')
    current_command = command[0]
    username = command[1]

    if current_command == 'register':
        license_plate = command[2]
        if username not in parking_list:
            parking_list[username] = license_plate
            print (f"{username} registered {parking_list[username]} successfully")
        else:
            print (f"ERROR: already registered with plate number {license_plate}")
    if current_command == 'unregister':
        if username in parking_list:
            del parking_list[username]
            print (f"{username} unregistered successfully")
        else:
            print (f"ERROR: user {username} not found")

for name in parking_list.keys():
    print (f"{name} => {parking_list[name]}")

