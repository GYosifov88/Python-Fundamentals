import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
highger_bonus = 0
higher_attendancies = 0


for i in range (number_of_students):
    attendancies = int(input())
    total_bonus = attendancies / number_of_lectures * (5 + additional_bonus)
    if total_bonus > highger_bonus:
        highger_bonus = total_bonus
        higher_attendancies = attendancies

print(f"Max Bonus: {math.ceil(highger_bonus)}.")
print(f"The student has attended {higher_attendancies} lectures.")
