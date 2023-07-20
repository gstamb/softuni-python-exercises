company_users = {}

while True:
    entry = input()
    if entry == "End":
        break

    company, employee = entry.split(" -> ")

    if company not in company_users:
        company_users[company] = []
        company_users[company].append(employee)
    else:
        if employee not in company_users[company]:
            company_users[company].append(employee)
        else:
            pass

for company, employees in company_users.items():
    print("{0}\n-- {1}".format(company, "\n-- ".join(employees)))
