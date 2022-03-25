activation_key = input()


command = input()

while command != 'Generate':
    current_command = command.split(">>>")
    action = current_command[0]
    if action == 'Contains':
        substring = current_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == 'Flip':
        letters_type = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        substring_to_change = activation_key[start_index:end_index]
        if letters_type == 'Lower':
            substring_to_change = substring_to_change.lower()
        elif letters_type == 'Upper':
            substring_to_change = substring_to_change.upper()
        activation_key = activation_key[:start_index] + substring_to_change + activation_key[end_index:]
        print(activation_key)
    elif action == 'Slice':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        activation_key = activation_key[0:start_index:] + activation_key[end_index::]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
