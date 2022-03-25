words = input().split(' ')
lower_word = list(map(lambda c: c.lower(), words))

occurrences = dict()

for word in lower_word:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

final_list = list()

for word in occurrences.keys():
    if occurrences[word] % 2 != 0:
        final_list.append(word)

print(" ".join(final_list))
