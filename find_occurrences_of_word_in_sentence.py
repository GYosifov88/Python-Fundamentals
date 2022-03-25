import re
text = input()
searched_word = input()

count = re.findall(rf'\b{searched_word}\b', text, re.IGNORECASE)

print(len(count))

