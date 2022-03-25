dictionary = dict()
command = input()
while "-" in command:
    entry = command.split("-")
    name = entry[0]
    number = entry[1]
    dictionary[name] = number

    command = input()

for i in range (int(command)):
    check = input()
    if check in dictionary.keys():
        print (f"{check} -> {dictionary[check]}")
    else:
        print (f"Contact {check} does not exist.")