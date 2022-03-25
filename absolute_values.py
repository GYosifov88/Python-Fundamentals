sequence = input().split(' ')
absolute_sequence = []

for digits in sequence:
    current_digit = abs(float(digits))
    absolute_sequence.append(current_digit)

print (absolute_sequence)