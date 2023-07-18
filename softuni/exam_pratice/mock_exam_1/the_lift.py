lift_queue = int(input())
lift_state = [int(x) for x in input().split()]

for wagon in range(len(lift_state)):
    while lift_state[wagon] < 4 and lift_queue > 0:
        lift_state[wagon] += 1
        lift_queue -= 1


if lift_queue == 0 and sum(lift_state) == len(lift_state) * 4:
    print(f"{' '.join([str(x) for x in lift_state])}")
elif lift_queue == 0:
    print("The lift has empty spots!")
    print(f"{' '.join([str(x) for x in lift_state])}")
elif lift_queue > 0 and sum(lift_state) == len(lift_state) * 4:
    print(f"There isn't enough space! {lift_queue} people in a queue!")
    print(f"{' '.join([str(x) for x in lift_state])}")


