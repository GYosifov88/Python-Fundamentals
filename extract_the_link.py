import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

links = list()
matches = re.finditer(r"\b[w]{3}\.([A-Za-z\.\-\d]+)\.[a-z]+", text)
for match in matches:
    links.append(match.group())

print('\n'.join(links))
