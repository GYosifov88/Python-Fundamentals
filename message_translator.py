import re

number_of_strings = int(input())
char_ascii_num_list = list()
pattern = r"\!(?P<command>[A-Z][a-z]{2,})\!:\[(?P<text>[A-Za-z]{8,})\]"

for i in range(number_of_strings):
    message = input()
    matches = re.match(pattern, message)
    if not matches:
        print("The message is invalid")
    else:
        mach_command = matches.group('command')
        for chr in matches.group('text'):
            char_ascii_num_list.append(str(ord(chr)))
        print(f"{mach_command}: {' '.join(char_ascii_num_list)}")
