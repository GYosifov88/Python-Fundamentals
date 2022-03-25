def chars_in_range(a, b):
    for n in range (ord(a) + 1, ord(b)):
        print(chr(n), end= ' ')


first_char = input()
second_char = input()

chars_in_range(first_char, second_char)