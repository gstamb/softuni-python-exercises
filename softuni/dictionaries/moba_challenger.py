players = {}

while True:

    entry = input()

    if entry == "Season end":
        break
    if entry.find(" vs ") != -1:
        player_one, player_two = entry.split(" vs ")
        if player_one in players and player_two in players:
            player_one_pos = [x for x in players[player_one].keys()]
            player_two_pos = [x for x in players[player_two].keys()]
            common = [x for x in player_one_pos if x in player_two_pos]
            if common:
                for position in common:
                    player_one_score = players[player_one][position]
                    player_two_score = players[player_two][position]
                    if player_one_score > player_two_score:
                        players[player_two].pop(position)

                        if len(players[player_two]) == 0:
                            players.pop(player_two)
                    elif player_two_score > player_one_score:
                        players[player_one].pop(position)

                        if len(players[player_one]) == 0:
                            players.pop(player_one)

        continue

    player, role, skill = entry.split(" -> ")
    if player in players:
        if role in players[player]:
            old_score = players[player][role]
            if old_score < int(skill):
                players[player][role] = int(skill)
        else:
            players[player][role] = int(skill)
    else:
        players[player] = {role: int(skill)}

scores = {}
for player, position in sorted(players.items(), key=lambda x: x):
    p, scr = player, sum(position.values())
    scores[p] = scr

for player, score in sorted(scores.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {score} skill")
    for role, skill in sorted(players[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {role} <::> {skill}")
