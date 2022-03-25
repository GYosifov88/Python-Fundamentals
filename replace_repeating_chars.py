import re
text = input()
new_text = re.sub(r"(.)\1+", r"\1",text)

print(new_text)
