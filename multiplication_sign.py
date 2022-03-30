def multiplication(first_num, second_num, third_num):
    positives = 0
    negatives = 0
    zeros = 0
    num_list = list()
    num_list.append(first_num)
    num_list.append(second_num)
    num_list.append(third_num)
    for num in num_list:
        if num == 0:
            zeros += 1
        elif num > 0:
            positives += 1
        elif int(num) < 0:
            negatives += 1

    if zeros > 0:
        print('zero')
    elif negatives % 2 == 0:
        print('positive')
    else:
        print('negative')


first_num = int(input())
second_num = int(input())
third_num = int(input())

multiplication(first_num, second_num, third_num)
