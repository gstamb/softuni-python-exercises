string = input()
list_chars = [x for x in string]

flag = False
n = 0
for index, value in enumerate(string):

    if value == ">":
        flag = True
    else:
        if flag:
            n += int(value)
            flag = False

            if n > 0:
                list_chars[index] = ""
                n -= 1

        elif n > 0:
            list_chars[index] = ""
            n -= 1
print("".join(list_chars))
