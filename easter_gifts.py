planned_gifts = input().split(' ')
final_list = []

command = input()
replacement_value = 'None'
while command != 'No Money':
    current_task = command.split(' ')
    task_type = current_task[0]
    current_gift = current_task[1]
    if task_type == 'OutOfStock':
        item_to_replace = current_gift
        indexes_to_replace = [i for i,x in enumerate(planned_gifts) if x==item_to_replace]
        for i in indexes_to_replace:
            planned_gifts[i] = replacement_value
    if task_type == 'Required':
        current_index = int(current_task[2])
        if 0 < current_index < (len(planned_gifts) - 1):
            planned_gifts[current_index] = current_gift

    if task_type == 'JustInCase':
        planned_gifts[-1] = current_gift

    command = input()

for k in planned_gifts:
    if 'None' in planned_gifts:
        planned_gifts.remove('None')

print(' '.join(planned_gifts))