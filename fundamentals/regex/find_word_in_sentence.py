import re

text = input()
target_word = input()

matches = re.findall(f""
                     f"\\b{target_word.lower()}\\b", text.lower())
print(len(matches))
