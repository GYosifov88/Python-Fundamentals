def palindrome ():
    sequence = input().split(', ')
    listing = list(map(int, sequence))
    for i in sequence:
        if i[0] == i[-1]:
            print('True')
        else:
            print('False')

palindrome()