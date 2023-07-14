start_char = input()
end_char = input()
string = input()

sum_of_chars = 0
min_val = ord(start_char)
max_val = ord(end_char)
for char in string:
    if min_val < ord(char) < max_val:
        sum_of_chars += ord(char)

print(sum_of_chars)
