def return_chars(a: chr, b: chr):
    start = ord(a)
    end = ord(b)

    result_string = ""
    for char in range(start + 1, end):
        result_string += chr(char) + " "

    return result_string


char_start, char_end = [input() for x in range(2)]
print(return_chars(char_start, char_end))
