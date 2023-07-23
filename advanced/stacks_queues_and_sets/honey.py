from collections import deque


def calculate_honey(load, capacity, operator):
    if operator == "+":
        return abs(load + capacity)
    elif operator == "-":
        return abs(load - capacity)
    elif operator == "/":
        return abs(load / capacity)
    elif operator == "*":
        return abs(load * capacity)


def match_nectar_bees(bees, nectar, honey_making):
    honey_made = 0

    while nectar and bees:
        bee_load = bees.popleft()
        nectar_capacity = nectar.pop()
        operator = ""
        if nectar_capacity >= bee_load:
            operator = honey_making.popleft()
        else:
            while nectar:
                nectar_capacity = nectar.pop()
                if nectar_capacity >= bee_load:
                    operator = honey_making.popleft()
                    break
            else:
                # need to re-insert the bee back else we impact the length of the bee queue upon exhausting nectar queue
                bees.appendleft(bee_load)

        if operator in ["-", "+", "/", "*"] and not (operator == '/' and nectar_capacity == 0):
            honey_made += calculate_honey(bee_load, nectar_capacity, operator)

    return honey_made


def main():
    bees = deque(map(int, input().split()))
    nectar = deque(map(int, input().split()))
    honey_making = deque(input().split())

    honey = match_nectar_bees(bees, nectar, honey_making)

    print(f"Total honey made: {honey}")
    if bees:
        print(f"Bees left: {', '.join([str(x) for x in bees])}")
    if nectar:
        print(f"Nectar left: {', '.join([str(x) for x in nectar])}")


if __name__ == "__main__":
    main()
