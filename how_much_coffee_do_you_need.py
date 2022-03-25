command = input()
number_of_coffees = 0


while True:

    if command == 'END':
        print(number_of_coffees)
        break

    if command.islower() and (command == 'cat' or command == 'dog' or command == 'movie' or command == 'coding'):
        number_of_coffees += 1
    elif command.isupper() and (command == 'CAT' or command == 'DOG' or command == 'MOVIE' or command == 'CODING'):
        number_of_coffees += 2
    else:
        number_of_coffees += 0
    if number_of_coffees > 5:
        print('You need extra sleep')
        break
    command = input()



