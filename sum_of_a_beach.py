import re
command = input()

ls1 = re.findall("fish", command, flags=re.IGNORECASE)
ls2 = re.findall("sun", command, flags=re.IGNORECASE)
ls3 = re.findall("water", command, flags=re.IGNORECASE)
ls4 = re.findall("sand", command, flags=re.IGNORECASE)
ls = ls4 + ls1 + ls3 + ls2

if not ls:
    print(0)
else:
    print(len(ls))