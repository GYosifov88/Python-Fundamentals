initial_text = input()

command = input()

while command != 'Finish':
    current_command = command.split(' ')
    action = current_command[0]

    if action == 'Replace':
        curr_chart = current_command[1]
        new_chart = current_command[2]
        initial_text = initial_text.replace(curr_chart, new_chart)
        print(initial_text)
    elif action == 'Cut':
        start_inx = int(current_command[1])
        end_inx = int(current_command[2])
        if 0 <= start_inx <= end_inx < len(initial_text):
            initial_text = initial_text[:start_inx] + initial_text[end_inx+1:]
            print(initial_text)
        else:
            print("Invalid indices!")
    elif action == 'Make':
        letters = current_command[1]
        if letters == 'Lower':
            initial_text = initial_text.lower()
        elif letters == 'Upper':
            initial_text = initial_text.upper()
        print(initial_text)
    elif action == 'Check':
        checked_text = current_command[1]
        if checked_text in initial_text:
            print(f"Message contains {checked_text}")
        else:
            print(f"Message doesn't contain {checked_text}")
    elif action == 'Sum':
        sum_chars = 0
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 <= start_index <= end_index < len(initial_text):
            substring = initial_text[start_index:end_index+1]
            for chr in substring:
                sum_chars += ord(chr)
            print(sum_chars)
        else:
            print("Invalid indices!")

    command = input()