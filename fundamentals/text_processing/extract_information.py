import re

for string in range(int(input())):
    string_to_process = input()

    pattern_name = "(?<=@)(.*?)(?=\|)"
    m = re.search(pattern_name, string_to_process)
    name = m.group(1)

    pattern_age = "(?<=#)(.*?)(?=\*)"
    m = re.search(pattern_age, string_to_process)
    age = m.group(1)

    print(f"{name} is {age} years old.")
