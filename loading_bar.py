def loading_bar(n):
    ready = ("%"*int(n/10))
    remain = ("."*int(10-n/10))
    loading_bara = ready+remain
    return loading_bara


n = int(input())
if n == 100:
    print(f'100% Complete!\n')
    print(f'[{loading_bar(n)}]')
else:
    print(f'{n}% [{loading_bar(n)}]')
    print(f'Still loading...')

# if number == 10:
#     print (f'{number}% [%.........]')
#     print('Still loading...')
# elif number == 20:
#     print (f'{number}% [%%........]')
#     print('Still loading...')
# elif number == 30:
#     print (f'{number}% [%%%.......]')
#     print('Still loading...')
# elif number == 40:
#     print (f'{number}% [%%%%......]')
#     print('Still loading...')
# elif number == 50:
#     print (f'{number}% [%%%%%.....]')
#     print('Still loading...')
# elif number == 60:
#     print (f'{number}% [%%%%%%....]')
#     print('Still loading...')
# elif number == 70:
#     print (f'{number}% [%%%%%%%...]')
#     print('Still loading...')
# elif number == 80:
#     print (f'{number}% [%%%%%%%%..]')
#     print('Still loading...')
# elif number == 90:
#     print (f'{number}% [%%%%%%%%%.]')
#     print('Still loading...')
# elif number == 100:
#     print ('100% Complete!')
#     print ('[%%%%%%%%%%]')
