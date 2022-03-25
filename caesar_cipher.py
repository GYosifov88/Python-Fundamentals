text = input()
incripted_text = ''

for char in text:
    new_char_ord = ord(char) + 3
    incripted_text += chr(new_char_ord)

print(incripted_text)
