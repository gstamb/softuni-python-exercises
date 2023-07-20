import re

demons = []
list_of_demons = sorted([x.strip() for x in input().split(",")])

for demon in list_of_demons:
    extract_letters = r"([^*+-./0-9])"
    extract_digits = r"([+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+)))"
    multipliers = r"([*/])"

    match_health = sum([ord(x) for x in re.findall(extract_letters, demon)])

    match_raw_damage = sum([float(x) for x in re.findall(extract_digits, demon)])

    multipliers = re.findall(multipliers, demon)

    if multipliers:
        for factor in multipliers:
            if factor == "*":
                match_raw_damage *= 2
            elif factor == "/":
                match_raw_damage /= 2

    demons.append(f"{demon} - {match_health:.0f} health, {match_raw_damage:.2f} damage")

for demon in demons:
    print(demon)


