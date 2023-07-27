from collections import deque

# keeps track on daily consumed coffeine. It should not exceed 300 or fall below 0.
CAFFEINE_INTAKE = 0


def main():
    global CAFFEINE_INTAKE
    # ingests two queues containing coffeine content and number of drinks
    caffeine_mg = list(map(int, input().split(", ")))
    energy_drinks_cnt = deque(list(map(int, input().split(", "))))

    # main loop that consumes elements of each queue
    while caffeine_mg and energy_drinks_cnt:
        caffeine_content = caffeine_mg.pop()
        energy_drinks = energy_drinks_cnt.popleft()

        # calculates caffeine intake and keeps track on total caffeine consumed.
        caffeine_intake = caffeine_content * energy_drinks
        if CAFFEINE_INTAKE + caffeine_intake <= 300:
            CAFFEINE_INTAKE += caffeine_intake
        else:
            # not ingesting the drink results in decreased levels of caffeine and return of the drink to the queue
            if CAFFEINE_INTAKE >= 30:
                CAFFEINE_INTAKE -= 30
            energy_drinks_cnt.append(energy_drinks)

    # prints the amount of drinks left and the caffeine level.
    if energy_drinks_cnt:
        print(f"Drinks left: {', '.join([str(x) for x in energy_drinks_cnt])}")
    else:
        print("At least Stamat wasn't exceeding the maximum caffeine.")

    print(f"Stamat is going to sleep with {CAFFEINE_INTAKE} mg caffeine.")


if __name__ == "__main__":
    main()
