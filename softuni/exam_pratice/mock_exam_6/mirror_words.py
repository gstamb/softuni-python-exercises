import re

input_string = input()

pattern = "(#[A-Za-z]{3,}##[A-Za-z]{3,}#|@[A-Za-z]{3,}@@[A-Za-z]{3,}@)"

matches = re.findall(pattern, input_string)
pairs = []
if matches:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        if match.startswith("@"):
            first, second = [x for x in match.split("@") if x != ""]
            if first == second[::-1]:
                pairs.append(f"{first} <=> {second}")
        else:
            first, second = [x for x in match.split("#") if x != ""]
            if first == second[::-1]:
                pairs.append(f"{first} <=> {second}")
else:
    print("No word pairs found!")

if pairs:
    print("The mirror words are:")
    print(", ".join(pairs))
else:
    print("No mirror words!")
