import re
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

matches = re.finditer(r"[0-9]+", text)
output = list()

for match in matches:
    output.append(match.group())

print(' '.join(output))