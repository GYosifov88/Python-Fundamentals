number = int(input())
searched_word = input()
full_list = []
searched_list = []
for word in range (number):
    current_string = input()
    full_list.append(current_string)
    if searched_word in current_string:
        searched_list.append(current_string)


print(full_list)

print(searched_list)