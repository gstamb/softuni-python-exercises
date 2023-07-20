string = input()
string1 = string.split()[0]
string2 = string.split()[1]

sum_of_chars_multiplied = 0

for char in range(min(len(string1), len(string2))):
    sum_of_chars_multiplied += ord(string1[char]) * ord(string2[char])

difference = len(string1) - len(string2)
if difference > 0:
    sum_of_chars_multiplied += sum([ord(x) for x in string1[len(string2):]])
if difference < 0:
    sum_of_chars_multiplied += sum([ord(x) for x in string2[len(string1):]])

print(sum_of_chars_multiplied)
