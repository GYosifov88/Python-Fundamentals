
dictionary = dict()

command = input()
command_counter = 0
while command != 'stop':
    command_counter +=1
    if command_counter % 2 != 0:
        resource = command
        if command not in dictionary:
            dictionary[resource] = 0
    else:
        quantity = int(command)
        if resource not in dictionary:
            dictionary[resource] = quantity
        else:
            dictionary[resource] += quantity


    command = input()


for resource in dictionary.keys():
    print (f"{resource} -> {dictionary[resource]}")

