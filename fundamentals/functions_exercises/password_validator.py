def validate_password(string: str):
    flag = []
    if 6 <= len(string) <= 10:
        flag.append(True)
    else:
        print("Password must be between 6 and 10 characters")

    if len([x for x in string if x.isalnum()]) == len(string):
        flag.append(True)
    else:
        print("Password must consist only of letters and digits")

    if len([x for x in string if x.isdigit()]) >= 2:
        flag.append(True)
    else:
        print("Password must have at least 2 digits")

    if len(flag) == 3:
        print("Password is valid")


login_input = input()
validate_password(login_input)
