initial_list = input().split(' ')
int_initial_list = list(map(int, initial_list))

average_amount = sum(int_initial_list) / len(int_initial_list)

new_list = [i for i in int_initial_list if i > average_amount]
final_list = sorted(list(map(str, new_list)), key=int, reverse=True)

if len(final_list) >0:
    if len(new_list) <= 5:
        print(' '.join(final_list))
    elif len(new_list) > 5:
        final_list = final_list[:5]
        print(' '.join(final_list))
else:
    print('No')