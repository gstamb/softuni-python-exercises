from collections import deque


def can_complete_circle(stations: list) -> int:
    fuel = 0
    while stations:
        # fuel consumption 1 fuel = 1 distance. Use popleft = FIFO
        fuel_refill_amount, distance_next_station = map(int, stations.popleft().split())
        if fuel + fuel_refill_amount >= distance_next_station:
            fuel += fuel_refill_amount - distance_next_station
        else:
            return False
    return True


def main():
    petrol_pumps = int(input())
    list_stations = [input() for x in range(petrol_pumps)]
    stations_stack = deque(list_stations)

    for pump in range(petrol_pumps):
        # need to create a shallow copy to avoid mutating the queue
        shallow_copy = deque([x for x in stations_stack])
        if can_complete_circle(shallow_copy):
            print(pump)
            break
        # rotate queue if not enough fuel to reach next station
        stations_stack.rotate(-1)


if __name__ == "__main__":
    main()
