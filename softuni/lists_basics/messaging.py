numbers = [int(x) for x in input().split()]
string = input()
string = [x for x in string]
new_string = ""
for num in numbers:
    strings_length = len(string)
    index_of_interest = sum([int(x) for x in str(num)])

    index_of_interest %= strings_length

    new_string += string[index_of_interest]
    string.pop(index_of_interest)

print(new_string)
