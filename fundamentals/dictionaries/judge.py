contests = {}
users = {}
order_contests = []


def add_score_user(usr: str, pts: str):
    if usr in users:
        users[usr] += int(pts)
    else:
        users[usr] = int(pts)


def index_gen():
    for i in range(1, 1000):
        yield i


while True:
    entry = input()
    if entry == "no more time":
        break
    else:
        name, contest, score = entry.split(" -> ")

        if contest not in contests:
            contests[contest] = {name: int(score)}
            add_score_user(name, score)
            order_contests.append(contest)
        else:
            if name in contests[contest]:
                old_score = contests[contest][name]
                if int(score) > old_score:
                    contests[contest][name] = int(score)
                    users[name] += int(score) - old_score

            else:
                contests[contest][name] = int(score)
                add_score_user(name, score)

for contest in order_contests:
    generator = index_gen()
    print(f"{contest}: {len(contests[contest])} participants")
    for participant, score in sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])):
        print(f"{next(generator)}. {participant} <::> {score}")

print("Individual standings:")
generator = index_gen()
for user, score in sorted(users.items(), key=lambda x: (-x[1], x[0])):
    print(f"{next(generator)}. {user} -> {score}")
