# def sum (a):
#     even_sum = 0
#     odd_sum = 0
#     new_list = [int(x) for x in str(a)]
#     for n in new_list:
#         if n % 2 == 0:
#             even_sum += n
#         else:
#             odd_sum += n
#     print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
#
# number = int(input())
#
# sum(number)

def odd_even_sum(nums):
    odd_sum = 0
    even_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


numbers = map(int, list(input()))
odd_even_sum(numbers)