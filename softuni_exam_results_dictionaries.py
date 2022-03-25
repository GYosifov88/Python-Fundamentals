courses = dict()
submissions = dict()
command = input()

while command != 'exam finished':
    current = command.split('-')
    username = current[0]
    language = current[1]

    if language != 'banned':
        points = int(current[2])
        if language not in courses:
            courses[language] = dict()
            submissions[language] = 1
            if username not in courses[language]:
                courses[language][username] = points
            else:
                if points >= courses[language][username]:
                    courses[language][username] = points
        else:
            submissions[language] += 1
            if username not in courses[language]:
                courses[language][username] = points
            else:
                if points >= courses[language][username]:
                    courses[language][username] = points
    elif language == 'banned':
        for ban in courses.keys():
            if username in courses[ban]:
                courses[ban].pop(username)

    command = input()

print('Results:')
for k in courses.keys():
    for j in courses[k]:
        print(f"{j} | {courses[k][j]}")

print('Submissions:')
for i in submissions.keys():
    print(f"{i} - {submissions[i]}")
