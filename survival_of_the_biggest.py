numbers = input().split(' ')
copy_list = list(map(int, numbers))
counter = int(input())

for _ in range (counter):
    current_min_element = min(copy_list)
    numbers.remove(str(current_min_element))
    copy_list.remove(current_min_element)

print (', '.join(numbers))