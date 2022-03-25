first_sequence = input().split(', ')
second_sequence = input()
final_list = [el for el in first_sequence if el in second_sequence]

print(final_list)