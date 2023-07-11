list_substrings = [x for x in input().split(", ")]
list_strings = [x for x in input().split(", ")]

result = [substring for substring in list_substrings if any(substring in string for string in list_strings)]
print(result)


# tarp, mice, bull
# lively, alive, harp, sharp, armstrong