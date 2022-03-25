import re
text = input()
output = list()
matches = re.finditer(r"(^| )([A-Za-z0-9]+[\.\_\-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", text)

for match in matches:
    output.append(match.group())

print('\n'.join(output))
