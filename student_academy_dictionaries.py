number_of_entries = int(input())
academy = {}

for num in range(number_of_entries):
    student_name = input()
    grade = float(input())
    if student_name not in academy:
        academy[student_name] = []
        academy[student_name].append(grade)
    else:
        academy[student_name].append(grade)

for k in academy.keys():
    average_grade = sum(academy[k]) / len(academy[k])
    if average_grade >= 4.50:
        print(f"{k} -> {average_grade:.2f}")