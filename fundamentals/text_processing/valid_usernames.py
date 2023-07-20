def isvalid(string: str) -> bool:
    for char in string:
        if char.isdigit() or char.isalpha() or char in legal:
            continue
        else:
            return False
    else:
        return True


legal = ["_", "-"]
potential_usernames = input().split(", ")
for username in potential_usernames:
    if 3 <= len(username) <= 16 and isvalid(username):
        print(username)
