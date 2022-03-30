numbers = input().split(' ')
text = input()
num_list = list()
sum_list = list()
new_text = ''

for i in numbers:
    num = int(i)
    num_list.append(i)

for j in num_list:
    digit_sum = 0
    for k in j:
        digit_sum += int(k)
    sum_list.append(digit_sum)

for p in sum_list:
    index = int(p)
    if 0 <= index < len(text):
        letter = text[index]
        new_text += letter
        text = text[:index] + text[index + 1:]
    else:
        letter = text[index-len(text)]
        new_text += letter
        text = text[:(index-len(text))] + text[(index-len(text)) + 1:]

print(new_text)
