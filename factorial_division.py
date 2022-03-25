# def factorial (a, b):
#     first_num = 1
#     second_num = 1
#     while a >= 1:
#         first_num = first_num * a
#         a -= 1
#     while b >= 1:
#         second_num = second_num * b
#         b -= 1
#     final_result = first_num / second_num
#     print (f'{final_result:.2f}')
#
#
# first_digit = int(input())
# second_digit = int(input())
#
# factorial(first_digit, second_digit)

def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num -1)


first_digit = int(input())
second_digit = int(input())
result = factorial(first_digit) / factorial(second_digit)
print(f'{result:.2f}')