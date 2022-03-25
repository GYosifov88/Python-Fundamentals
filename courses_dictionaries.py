def course_info ():

    university = dict()
    command = input()

    while command != 'end':
        current_case = command.split(" : ")
        course = current_case[0]
        name = current_case[1]
        if course not in university:
            university[course] = []
            university[course].append(name)
        else:
            university[course].append(name)

        command = input()
    for course in university.keys():
        print (f"{course}: {len(university[course])}")
        for name in university[course]:
            print (f"-- {name}")

course_info()