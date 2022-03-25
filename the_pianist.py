number_of_pieces = int(input())
song_list = dict()

for n in range (number_of_pieces):
    pieces = input().split('|')
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]
    song_list[piece]= list()
    song_list[piece].append(composer)
    song_list[piece].append(key)

command = input()
while command != 'Stop':
    current_command = command.split('|')
    action = current_command[0]
    current_piece = current_command[1]

    if action == 'Add':
        new_composer = current_command[2]
        new_key = current_command[3]
        if current_piece not in song_list.keys():
            song_list[current_piece] = list()
            song_list[current_piece].append(new_composer)
            song_list[current_piece].append(new_key)
            print(f"{current_piece} by {new_composer} in {new_key} added to the collection!")
        else:
            print(f"{current_piece} is already in the collection!")

    if action == 'Remove':
        if current_piece in song_list.keys():
            del song_list[current_piece]
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    if action == 'ChangeKey':
        new_keys = current_command[2]
        if current_piece in song_list.keys():
            song_list[current_piece].pop(-1)
            song_list[current_piece].append(new_keys)
            print(f"Changed the key of {current_piece} to {new_keys}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    command = input()

for j in song_list.keys():
    print(f"{j} -> Composer: {song_list[j][0]}, Key: {song_list[j][1]}")