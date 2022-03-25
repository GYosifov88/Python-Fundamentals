numbers_list = input().split(', ')
new_list = []

for digit in numbers_list:
    digits = digit.split(', ')
    current_digit = int(digits[0])
    if current_digit == 0:
        numbers_list.remove('0')
        numbers_list.append('0')
new_list = list(map(int, numbers_list))
print(new_list)
