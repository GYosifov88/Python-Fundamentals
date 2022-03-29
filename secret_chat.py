secret_message = input()

command = input()

while command != 'Reveal':
    current_command = command.split(':|:')
    action = current_command[0]

    if action == 'InsertSpace':
        index = int(current_command[1])
        secret_message = secret_message[:index] + ' ' + secret_message[index:]
        print(secret_message)

    elif action == 'Reverse':
        substring = current_command[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, '', 1)
            substring = substring[::-1]
            secret_message = secret_message + substring
            print(secret_message)
        else:
            print('error')

    elif action == 'ChangeAll':
        old_str = current_command[1]
        new_str = current_command[2]
        secret_message = secret_message.replace(old_str, new_str)
        print(secret_message)

    command = input()

print(f"You have a new text message: {secret_message}")
