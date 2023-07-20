import re


def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return numbers


def capture_numbers():
    extracted_numbers = []
    while True:
        line = input()
        if line.strip() == "":
            break
        extracted_numbers.extend(extract_numbers(line))

    numbers_str = ' '.join(extracted_numbers)
    print(numbers_str)


capture_numbers()
