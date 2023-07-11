version = [x for x in input().split(".")]
new_vers = [x for x in str(int("".join(version)) +1) ]
print(".".join(new_vers))

