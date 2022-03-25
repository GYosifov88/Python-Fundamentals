needed = {'shards': 0, "fragments": 0, "motes": 0}
junk = dict()
is_obtained = False

while True:
    materials = input().split(" ")
    materials_list = list(map(lambda c: c.lower(), materials))
    for i in range(0, len(materials_list), 2):
        quantity = int(materials_list[i])
        word = materials_list[i+1]
        if word == "shards":
            needed["shards"] += quantity
            if needed['shards'] >= 250:
                needed['shards'] -= 250
                print("Shadowmourne obtained!")
                is_obtained = True
                break
        elif word == "fragments":
            needed["fragments"] += quantity
            if needed["fragments"] >= 250:
                needed["fragments"] -= 250
                print("Valanyr obtained!")
                is_obtained = True
                break
        elif word == "motes":
            needed["motes"] += quantity
            if needed["motes"] >= 250:
                needed["motes"] -= 250
                print("Dragonwrath obtained!")
                is_obtained = True
                break
        else:
            if word not in junk:
                junk[word] = quantity
            else:
                junk[word] += quantity

    if is_obtained == True:
        for j in needed.keys():
            print(f"{j}: {needed[j]}")
        for k in junk.keys():
            print(f"{k}: {junk[k]}")
        break


