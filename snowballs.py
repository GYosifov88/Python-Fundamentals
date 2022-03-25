import sys

number_of_snowballs = int(input())
highest_value = -sys.maxsize
highest_quality = -sys.maxsize
highest_weight = -sys.maxsize
highest_time = -sys.maxsize


for i in range (number_of_snowballs):
    weight_of_snowball = int(input())
    time_of_reaching = int(input())
    quality_of_snowball = int(input())
    current_snowball_value = (weight_of_snowball / time_of_reaching) ** quality_of_snowball
    if current_snowball_value > highest_value:
        highest_value = current_snowball_value
        highest_weight = weight_of_snowball
        highest_quality = quality_of_snowball
        highest_time = time_of_reaching


print(f"{highest_weight} : {highest_time} = {highest_value:.0f} ({highest_quality:.0f})")
