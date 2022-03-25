# def even_num(a):
#     even_list = []
#     for i in numbers:
#         nm = i.split(' ')
#         num = int(nm[0])
#         if num % 2 == 0:
#             even_list.append(int(i))
#
#     print(even_list)
#
# numbers = input().split(' ')
# even_num(numbers)


result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
print(result)