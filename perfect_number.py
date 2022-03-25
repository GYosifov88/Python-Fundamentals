def perfect_number(a):
    divisor_list = []
    for i in range (1, a + 1):
        if a % i == 0:
            divisor_list.append(i)
    if sum(map(int, divisor_list)) / 2 == a:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)