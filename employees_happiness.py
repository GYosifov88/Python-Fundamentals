employees_happiness = input().split(' ')
employees_happiness = list(map(int, employees_happiness))
factor = int(input())

happy_employees = list(filter(lambda emp: emp >= sum(employees_happiness) / len(employees_happiness), employees_happiness))

if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")