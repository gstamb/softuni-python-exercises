while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:
        result = [x * 2 for x in string]
        print("".join(result))
