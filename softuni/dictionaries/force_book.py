force_book = {}


def check_if_exists(usr: str):
    for key, value in force_book.items():
        for player in value:
            if player == usr:
                return key
    else:
        return None


def append_user(side, user):
    if side in force_book:
        force_book[side].append(user)
    else:
        force_book[side] = []
        force_book[side].append(user)


while True:
    entry = input()
    if entry == "Lumpawaroo":
        break
    if entry.find("|") > 0:
        side, user = entry.split(" | ")

        if side not in force_book and check_if_exists(user) is None:
            append_user(side, user)
        else:
            if check_if_exists(user):
                continue
            else:
                force_book[side].append(user)

    else:
        user, side = entry.split(" -> ")
        side_existing_user = check_if_exists(user)
        if side_existing_user:
            force_book[side_existing_user].remove(user)
            append_user(side, user)
        else:
            append_user(side, user)
        print(f"{user} joins the {side} side!")

for force_side, users in force_book.items():
    if users:
        print("Side: {0}, Members: {1}\n! {2}".format(force_side, len(users), "\n! ".join(users)))
