text = input().split(' ')
result = [word for word in text if len(word) % 2 == 0]
print('\n'.join(result)) # with '\n' we are printing each on new row
