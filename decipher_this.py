secret_message = input().split(' ')
new_list = []
final_list = []
for word in secret_message:
    removed_digits = ''
    for i in word:
        if i.isdigit():
            removed_digits += i
            word = word.replace(i, "")
    word = chr(int(removed_digits)) + word
    new_list.append(word)

for word in new_list:
    word_temp = list(word)
    word_temp[1], word_temp[-1] = word_temp[-1], word_temp[1]
    word = ''.join(word_temp)
    final_list.append(word)
print(' '.join(final_list))
