import re

text = input()

matches = re.finditer(r"\b(_{1})(?P<variable>[A-Za-z\d]+)\b", text)

variables_list = list()

for match in matches:
    variable = match.group('variable')
    variables_list.append(variable)


print(','.join(variables_list))
