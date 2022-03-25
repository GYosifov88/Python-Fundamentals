import re

text = input()

matches = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))", text)

output = list()

for match in matches:
    output.append(match.group())

print(' '.join(output))
