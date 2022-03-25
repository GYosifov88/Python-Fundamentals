text = input()
vowel_list = ['a', 'o', 'u', 'e', 'i']
new_list = [x for x in text if x not in vowel_list]

print(''.join(new_list))