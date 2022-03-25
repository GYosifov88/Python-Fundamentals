def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c

first_num = int(input())
second_num = int(input())
third_num = int(input())
result = subtract(sum_numbers(first_num, second_num), third_num)
print(result)




