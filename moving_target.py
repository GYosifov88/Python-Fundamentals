target = input().split(' ')
targe_nums = list(map(int, target))
is_target_shot = False
command = input()
new_list = []
while command != "End":
    current_task = command.split(' ')
    action = current_task[0]
    index = int(current_task[1])
    if action == 'Shoot':
        power = int(current_task[2])
        if -1 < index <= len(target):
            targe_nums[index] -= power
            if targe_nums[index] <=0:
                targe_nums.pop(index)
    if action == 'Add':
        value = int(current_task[2])
        if -1 < index <= len(target):
            targe_nums.insert(index, value)
        else:
            print("Invalid placement!")
    if action == 'Strike':
        radius = int(current_task[2])
        if index in range (len(targe_nums)) and (index + radius) in range(len(targe_nums)) and (index - radius) in range(len(targe_nums)):
            del targe_nums[(index - radius):(index+radius+1)]

        else:
            print("Strike missed!")


    command = input()

targe_nums_final = [str(a) for a in targe_nums]

print('|'.join(targe_nums_final))