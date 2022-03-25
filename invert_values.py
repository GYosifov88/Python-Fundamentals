initial_list = input()
multiplied_list = []

my_list = initial_list.split(" ")

for i in my_list:
    multiplied_list.append(int(i) *-1)

print(multiplied_list)