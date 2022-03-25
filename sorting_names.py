names_list = input().split(', ')

sorted_list = sorted(names_list)
sorted_list = sorted(sorted_list, key=lambda x: -len(x))

print(sorted_list)