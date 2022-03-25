text = input()
digits = ''
letters = ''
symbols = ''

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalnum():
        letters += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)
