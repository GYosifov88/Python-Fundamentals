string = input()

my_list = string.split(", ")
last_position = my_list[-1]
number_of_animals = len(my_list)
element = 'wolf'
position_of_wolf = my_list.index(element)
position_of_treaten_sheep = abs(position_of_wolf + 1 - len(my_list))
if last_position == "wolf":
    print ("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {position_of_treaten_sheep}! You are about to be eaten by a wolf!")

