def data_types (a, b):
    if a == 'int':
        print (int(b) * 2)
    elif a == 'real':
        result = float(b) * 1.5
        print (f'{result:.2f}')
    elif a == 'string':
        print(f'${b}$')

command = input()
type = input()

data_types(command, type)