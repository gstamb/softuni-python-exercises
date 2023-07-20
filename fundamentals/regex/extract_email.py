import re

text = input()
pattern = r"((^|(?<=\s))([a-zA-Z0-9]+[-_.]?[a-zA-Z0-9]+)(?=@)(?:@)([a-zA-Z0-9]+([_.-][a-zA-Z]+)+)(\b|(?=\s)))"
matches = re.findall(pattern, text)
for match in matches:
    print(match[0])

