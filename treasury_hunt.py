initial_loot = input().split("|")
average_gain = 0
stolen_list = []
command = input()
treasury_hunt_not_failed = True
while command != "Yohoho!":
    action = command.split(' ')
    current_action = action.pop(0)

    if current_action == 'Loot':
        for i in action:
            if i not in initial_loot:
                initial_loot.insert(0, i)
    if current_action == 'Drop':
        index_of_item_to_remove = action[0]
        if int(index_of_item_to_remove) in range (len(initial_loot)):
            removed_item = initial_loot[int(index_of_item_to_remove)]
            initial_loot.pop(int(index_of_item_to_remove))
            initial_loot.append(removed_item)
    if current_action == 'Steal':
        stolen_list = []
        count_of_stolen_items = action[0]
        for k in range (int(count_of_stolen_items)):
            if initial_loot:
                stolen_item = initial_loot[-1]
                stolen_list.insert(0, stolen_item)
                initial_loot.pop(-1)
        print(', '.join(stolen_list))
    if len(initial_loot) <= 0:
        print("Failed treasure hunt.")
        treasury_hunt_not_failed = False
        break

    command = input()

    sum_of_chars = sum(len(i) for i in initial_loot)
    average_gain = sum_of_chars / len(initial_loot)


if treasury_hunt_not_failed:
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

# loot = input().split('|')
# sum_items = 0
#
# while True:
#     command = input().split()
#     if command[0] == 'Yohoho!':
#         break
#
#     elif command[0] == 'Loot':
#         for i in range(len(command)):
#             if i == 0:
#                 continue
#             item = command[i]
#             if item not in loot:
#                 loot.insert(0, item)
#
#     elif command[0] == 'Drop':
#         idx = int(command[1])
#         if 0 <= idx < len(loot):
#             x = loot.pop(idx)
#             loot.append(x)
#         else:
#             continue
#
#     elif command[0] == 'Steal':
#         n = int(command[1])
#         if n >= len(loot):
#             removed = loot
#             print(', '.join(removed))
#             print('Failed treasure hunt.')
#             exit()
#         else:
#             removed = loot[-n:]
#             del loot[-n:]
#             print(', '.join(removed))
#
# if len(loot) > 0:
#     for i in range(len(loot)):
#         sum_items += len(loot[i])
