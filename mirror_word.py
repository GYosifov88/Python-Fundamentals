import re

text = input()
pattern = r'(\@|\#)(?P<firstword>[A-Za-z]{3,})\1{2}(?P<secondword>[A-Za-z]{3,})\1'
mirror_words = dict()
first_words = list()
second_words = list()
mirror_list = list()
matches = re.finditer(pattern, text)

for match in matches:
    first = match.group('firstword')
    second = match.group('secondword')
    first_words.append(first)
    second_words.append(second)
    if second[::-1] == first:
        mirror_words[first] = second

for word in mirror_words:
    pair = word + ' <=> ' + mirror_words[word]
    mirror_list.append(pair)

if len(first_words) == 0 and len(second_words) == 0:
    print("No word pairs found!")
else:
    print(f"{len(first_words)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_list))
