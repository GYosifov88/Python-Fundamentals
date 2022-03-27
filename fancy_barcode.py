import re

number = int(input())
regex = r"@#+(?P<item>[A-Z][a-zA-Z0-9]{4,}[A-Z])"
for i in range(number):
    barcode = input()
    match = re.search(regex, barcode)
    if not match:
        print("Invalid barcode")
    else:
        barcod = match.group('item')
        group_nums = [char for char in barcod if char.isdigit()] or '00'
        print(f"Product group: {''.join(group_nums)}")



