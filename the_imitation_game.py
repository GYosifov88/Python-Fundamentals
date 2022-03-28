text = input()

command = input()

while command != 'Decode':
    current_command = command.split('|')
    action = current_command[0]

    if action == 'Move':
        num_of_letters = int(current_command[1])
        substring = text[:num_of_letters]
        text = text[num_of_letters:] + substring

    elif action == 'Insert':
        index = int(current_command[1])
        new_value = current_command[2]
        text = text[:index] + new_value + text[index:]

    elif action == 'ChangeAll':
        substring = current_command[1]
        replacement = current_command[2]
        text = text.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {text}")
