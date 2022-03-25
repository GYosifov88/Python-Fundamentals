cards_deck = input().split(', ')
number = int(input())

for card in range (number):
    command = input().split(', ')
    current_command = command[0]

    if current_command == 'Add':
        new_card = command[1]
        if new_card not in cards_deck:
            cards_deck.append(new_card)
            print('Card successfully added')
        else:
            print('Card is already in the deck')
    elif current_command == 'Remove':
        new_card = command[1]
        if new_card in cards_deck:
            cards_deck.remove(new_card)
            print('Card successfully removed')
        else:
            print('Card not found')
    elif current_command == 'Remove At':
        index = int(command[1])
        if 0 <= index < len(cards_deck):
            cards_deck.pop(index)
            print('Card successfully removed')
        else:
            print('Index out of range')
    elif current_command == 'Insert':
        index = int(command[1])
        new_card = command[2]
        if 0 <= index < len(cards_deck):
            if new_card not in cards_deck:
                cards_deck.insert(index, new_card)
                print('Card successfully added')
            else:
                print('Card is already added')
        else:
            print('Index out of range')

print(', '.join(cards_deck))
