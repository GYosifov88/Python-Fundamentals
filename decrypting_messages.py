key = int(input())
number_of_chars = int(input())
new_letter = ''
text = ''
for char in range (number_of_chars):
    letters = input()
    new_letter = ord(letters) + key
    char_new_letter = chr(new_letter)
    print(f'{char_new_letter}', end='')
