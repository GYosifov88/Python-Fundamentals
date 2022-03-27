import re

text = input()
regex = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)"

matches = re.findall(regex, text)

threshold_sum = 1
digits = [x for x in text if x.isdigit()]

for j in digits:
    threshold_sum *= int(j)

cool_emoji_list = []

for emoji in matches:
    coolness_sum = 0
    for ch in emoji[1]:
        coolness_sum += ord(ch)
    if coolness_sum >= threshold_sum:
        cool_emoji_list.append(emoji)

print(f"Cool threshold: {threshold_sum}")

print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in cool_emoji_list:
    print(''.join(emoji))
