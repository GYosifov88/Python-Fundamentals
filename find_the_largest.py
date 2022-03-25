number = input()
new_list = list(map(int, number))
final_list = sorted(list(map(str, new_list)), key=int, reverse=True)
print(''.join(final_list))