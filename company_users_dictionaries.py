def company_list():
    company = dict()

    command = input()
    while command != 'End':
        current = command.split(' -> ')
        company_name = current[0]
        employee_id = current[1]

        if company_name not in company:
            company[company_name] = []
            if employee_id not in company[company_name]:
                company[company_name].append(employee_id)
        else:
            if employee_id not in company[company_name]:
                company[company_name].append(employee_id)
        command = input()

    for k in company.keys():
        print(k)
        for id in company[k]:
            print(f'-- {id}')

company_list()