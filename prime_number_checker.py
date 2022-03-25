number = int(input())
is_number_prime = True
if number > 1:
    for i in range (2, number):
        if number % i == 0:
            is_number_prime = False

if is_number_prime == True:
    print ('True')
else:
    print ('False')