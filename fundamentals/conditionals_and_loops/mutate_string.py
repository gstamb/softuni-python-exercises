string_first = input()
string_second = input()

for i in range(len(string_second)):
    if string_first[i] != string_second[i]:
        string_first = string_first[:i] + string_second[i] + string_first[i + 1:]
        print(string_first)