from collections import Counter

string = [x for x in input() if x != " "]
keys = Counter(string).keys()
values = Counter(string).values()
result_dict = dict(zip(keys, values))

for key, value in result_dict.items():
    print(f"{key} -> {value}")
