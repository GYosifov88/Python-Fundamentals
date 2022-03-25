first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
fourth_digit = int(input())

sum_first_second = first_digit + second_digit
divide = int(sum_first_second / third_digit)
multiply = divide * fourth_digit

print(f'{multiply:.0f}')
