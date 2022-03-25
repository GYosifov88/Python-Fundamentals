deck = input().split(' ')
count_of_shuffles = int(input())

lenght_of_deck = len(deck)
middle_of_deck = int(lenght_of_deck / 2)

for i in range (0, count_of_shuffles):
    current_deck = []
    for p in range (0, middle_of_deck):
        current_deck.append(deck[p])
        current_deck.append(deck[middle_of_deck])
        middle_of_deck += 1
    deck = current_deck
    middle_of_deck = int(lenght_of_deck / 2)
print(current_deck)
