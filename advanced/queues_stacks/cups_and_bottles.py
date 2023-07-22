from collections import deque


def fillup_cup(cups_queue: deque, bottles_queue: deque) -> int:
    cup_vol = cups_queue.popleft()
    bottle_vol = bottles_queue.pop()

    if bottle_vol > cup_vol:
        waste = bottle_vol - cup_vol
        return waste
    elif bottle_vol == cup_vol:
        return 0
    else:
        # if cup's size is larger than the volume of the bottle insert the cup in front of the queue
        cup_vol -= bottle_vol
        cups_queue.appendleft(cup_vol)
        return 0


def main():
    cups = deque([int(x) for x in input().split()])
    bottles = deque([int(x) for x in input().split()])
    wasted_water = 0

    while cups and bottles:
        wasted_water += fillup_cup(cups, bottles)

    if not cups:
        print(f"Bottles: {' '.join([str(x) for x in bottles])}")
        print(f"Wasted litters of water: {wasted_water}")
    elif not bottles:
        print(f"Cups: {' '.join([str(x) for x in cups])}")
        print(f"Wasted litters of water: {wasted_water}")


if __name__ == "__main__":
    main()
