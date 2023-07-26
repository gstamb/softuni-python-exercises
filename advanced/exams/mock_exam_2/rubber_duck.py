from collections import deque


def main():
    """
    The program keeps track to rubber ducks given to programmers based the amount worked on a task.
    Uses Deque and a list to hold data. It runs until the programmers and tasks queues are empty.
    Prints the exit message and amount of ducks allocated in the end.

    Programmers queue holds the number of tasks; time_per_task contains hour per each task
    """
    programmers = deque(map(int, input().split()))
    time_per_task = list(map(int, input().split()))

    rubber_ducks_given = []
    ducks = {60: "Darth Vader Ducky",
             120: "Thor Ducky",
             180: "Big Blue Rubber Ducky",
             240: "Small Yellow Rubber Ducky"}

    while programmers and time_per_task:
        queue_programmer = programmers.popleft()
        hours_needed = time_per_task.pop()

        hours_worked = queue_programmer * hours_needed
        if 181 <= hours_worked < 241:
            rubber_ducks_given.append(ducks[240])
        elif 121 <= hours_worked < 181:
            rubber_ducks_given.append(ducks[180])
        elif 61 <= hours_worked < 121:
            rubber_ducks_given.append(ducks[120])
        elif 0 <= hours_worked < 61:
            rubber_ducks_given.append(ducks[60])
        else:
            hours_needed -= 2
            time_per_task.append(hours_needed)
            programmers.append(queue_programmer)

    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
    print(f"Darth Vader Ducky: {sum(1 for x in rubber_ducks_given if x == ducks[60])}")
    print(f"Thor Ducky: {sum(1 for x in rubber_ducks_given if x == ducks[120])}")
    print(f"Big Blue Rubber Ducky: {sum(1 for x in rubber_ducks_given if x == ducks[180])}")
    print(f"Small Yellow Rubber Ducky: {sum(1 for x in rubber_ducks_given if x == ducks[240])}")


if __name__ == "__main__":
    main()
