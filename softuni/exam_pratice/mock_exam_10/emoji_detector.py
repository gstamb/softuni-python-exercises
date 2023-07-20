import re
from functools import reduce

string = input()

pattern_emoji = "(\:\:[A-Z][a-z]{2,}\:\:|\*\*[A-Z][a-z]{2,}\*\*)"
pattern_digits = r"(\d+)"

match_emoji = re.findall(pattern_emoji, string)

match_digits = re.findall(pattern_digits, string)

coolness = "".join(match_digits)
cool_threshold = reduce(lambda a, b: a * b, [int(x) for x in coolness])
print(f"Cool threshold: {cool_threshold}")
print(f"{len(match_emoji)} emojis found in the text. The cool ones are:")
for emoji in match_emoji:
    temp = ""
    if emoji.startswith(":"):
        temp = emoji.strip(":")
    else:
        temp = emoji.strip("*")
    if sum([ord(x) for x in temp]) > cool_threshold:
        print(emoji)
