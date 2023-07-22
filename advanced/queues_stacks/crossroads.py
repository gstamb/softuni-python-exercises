from collections import deque


def evaluate_crossing(green_light_window, cars_queue, free_window, len_passed_cars):
    """ Keeps track on how many cars have passed and whether a crash has occurred. """
    next_car = None
    remaining_secs = green_light_window
    while cars_queue:
        next_car = cars_queue.popleft()
        remaining_secs -= len(next_car)
        len_passed_cars.append(len(next_car))
        if remaining_secs <= 0:
            break

    if remaining_secs + free_window < 0:
        len_passed_cars.pop()
        print("A crash happened!")
        print(f"{next_car} was hit at {next_car[green_light_window + free_window - sum(len_passed_cars)]}.")
        return True


def main():
    green_light_window = int(input())
    free_window = int(input())

    cars_queue = deque()
    len_passed_cars = deque()

    while True:
        instruction = input()
        if instruction == "END":
            print("Everyone is safe.")
            print(f"{len(len_passed_cars)} total cars passed the crossroads.")
            break

        if instruction == "green":
            # if there has been a crash break the loop
            if evaluate_crossing(green_light_window, cars_queue, free_window, len_passed_cars):
                break
        else:
            cars_queue.append(instruction)


if __name__ == "__main__":
    main()
