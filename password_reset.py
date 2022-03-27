text = input()
new_pass = ''
command = input()

while True:
    current_command = command.split(' ')
    action = current_command[0]

    if action == 'Done':
        print(f"Your password is: {text}")
        break

    elif action == 'TakeOdd':
        for ch in range(len(text)):
            if ch % 2 != 0:
                new_pass += text[ch]
        text = new_pass
        print(text)

    elif action == 'Cut':
        index = int(current_command[1])
        lenght = int(current_command[2])
        subs = text[index:(index + lenght)]
        text = text.replace(subs, '', 1)
        print(text)

    if action == 'Substitute':
        substring = current_command[1]
        substitute = current_command[2]
        if substring not in text:
            print("Nothing to replace!")
        else:
            text = text.replace(substring, substitute)
            print(text)

    command = input()


