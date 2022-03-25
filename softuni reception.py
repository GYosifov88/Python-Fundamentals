first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_of_students = int(input())
dealt_students = 0
hours_needed = 0

total_student_answered_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while number_of_students > 0:
    hours_needed += 1
    if hours_needed % 4 == 0:
        continue

    number_of_students -= total_student_answered_per_hour


print (f"Time needed: {hours_needed}h.")
