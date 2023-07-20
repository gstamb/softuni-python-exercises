waypoints = [int(x) for x in input().split()]
midway = len(waypoints) // 2
left = waypoints[:midway]
right = waypoints[midway + 1:]
right.reverse()

score_left = 0
score_right = 0

for waypoint in range(len(left)):
    if left[waypoint] != 0:
        score_left += left[waypoint]
    else:
        score_left *= 0.8

    if right[waypoint] != 0:
        score_right += right[waypoint]
    else:
        score_right *= 0.8


if score_left < score_right:
    print(f"The winner is left with total time: {score_left:.1f}")
else:
    print(f"The winner is right with total time: {score_right:.1f}")
