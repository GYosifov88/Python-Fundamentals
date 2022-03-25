current_version = input().split('.')
first_digit = int(current_version[0])
second_digit = int(current_version[1])
third_digit = int(current_version[2])

if 0 <= third_digit < 9:
    print(f'{first_digit}.{second_digit}.{third_digit+1}')
if third_digit == 9 and second_digit != 9:
    print(f'{first_digit}.{second_digit+1}.{10 - (third_digit + 1)}')
if third_digit == 9 and second_digit == 9:
    print(f'{first_digit+1}.{10 - (second_digit + 1)}.{10 - (third_digit + 1)}')


# another way
# def next_version(version_number):
#     version_number = int(''.join(version_number)) + 1
#     result = [str(num) for num in str(version_number)]
#     print('.'.join(result))
#
#
# data = input().split('.')
# next_version(data)