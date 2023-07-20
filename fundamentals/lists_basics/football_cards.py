sent_off_players = [x for x in input().split()]
# players_left_a = 11 - len({x for x in sent_off_players if "A" in x and 1 <= int(x[2:]) <= 11})
# players_left_b = 11 - len({x for x in sent_off_players if "B" in x and 1 <= int(x[2:]) <= 11})
#
# print(f"Team A - {players_left_a}; Team B - {players_left_b}")
# if players_left_b < 7 or players_left_a < 7:
#     print("Game was terminated")


players_left_a = 11
players_left_b = 11
already_sent_off = []

for player in sent_off_players:
    if "A" in player and player not in already_sent_off:
        players_left_a -= 1
        already_sent_off.append(player)
    if "B" in player and player not in already_sent_off:
        players_left_b -= 1
        already_sent_off.append(player)
    if players_left_a < 7 or players_left_b < 7:
        break

print(f"Team A - {players_left_a}; Team B - {players_left_b}")
if players_left_b < 7 or players_left_a < 7:
    print("Game was terminated")
