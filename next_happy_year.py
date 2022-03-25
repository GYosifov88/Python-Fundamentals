year = int(input())

is_hapyy_year = False

while not is_hapyy_year:
    year += 1
    str_year = str(year)
    set_year = set(str_year)

    if len(str_year) == len(set_year):
        is_hapyy_year = True
print(year)

