force_list = dict()

command = input()

while command != 'Lumpawaroo':
    if '|' in command:
        current = command.split(' | ')
        force_side = current[0]
        force_user = current[1]
        condition = [current for current in force_list if force_user in force_list[current]]
        if len(condition) == 0:
            condition.clear()
            if force_side not in force_list:
                force_list[force_side] = [force_user]
            else:
                force_list[force_side].append(force_user)

    elif '->' in command:
        current = command.split(' -> ')
        force_side = current[1]
        force_user = current[0]
        for side in force_list:
            if force_user in force_list[side]:
                if len(force_list[side]) > 1:
                    force_list[side].remove(force_user)
                    break
                else:
                    del force_list[side]
                    break

        if force_side in force_list:
            force_list[force_side].append(force_user)
        else:
            force_list[force_side] = [force_user]

        print(f"{force_user} joins the {force_side} side!")

    command = input()


for j in force_list:
    if len(force_list[j]) > 0:
        print(f"Side: {j}, Members: {len(force_list[j])}")
        for person in force_list[j]:
            print(f"! {person}")