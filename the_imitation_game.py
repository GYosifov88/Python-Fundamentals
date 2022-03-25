text = input()
encrypted_message = list(text)

command = input()

while command != 'Decode':
    current_command = command.split('|')
    action = current_command[0]

    if action == 'Move':
        num_of_letters = int(current_command[1])
        for j in range (num_of_letters):
            encrypted_message += [encrypted_message.pop(0)]
    if action == 'Insert':
        index = int(current_command[1])
        new_value = current_command[2]
        encrypted_message.insert(index, new_value)
    if action == 'ChangeAll':
        substring = current_command[1]
        replacement = current_command[2]
        encrypted_message = [replacement if x == substring else x for x in encrypted_message]

    command = input()

print(f"The decrypted message is: {''.join(encrypted_message)}")
