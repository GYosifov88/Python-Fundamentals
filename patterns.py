num = int(input())

for columns in range (1, num + 1):
    for rows in range (0, columns):
        print('*', end='')
    print()
for columns in range (num - 1 , 0, -1):
    for rows in range (0, columns):
        print('*', end='')
    print()