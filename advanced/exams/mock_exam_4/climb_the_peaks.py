from collections import deque


def main():
    """ A climber attempts to conquer the five most difficult peaks in Pirit mountain in 7 days
        At his disposal are food and stamina the sum of which is matched against the difficulty of a peak.
        Peaks are attempted in a sequential order until there either no food or stamina left or there are no peaks to climb
        If climber manages to conquer all the peaks, a message is displayed alongside the number of peaks conquered
        in the order of climbing.
        Else another message is displayed.
        """

    # parses food and stamina inputs
    food = list(map(int, input().split(", ")))
    stamina = deque(list(map(int, input().split(", "))))

    # list of each mountain to climb and corresponding difficulty
    mountain_peaks = {
        "Vihren": 80,
        "Kutelo": 90,
        "Banski Suhodol": 100,
        "Polezhan": 60,
        "Kamenitza": 70
    }

    # sequential order of the attempts
    peaks_queue = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])

    # main loop that consumes elements of each queue
    while food and stamina and peaks_queue:
        food_consumed = food.pop()
        stamina_consumed = stamina.popleft()

        next_peak = peaks_queue.popleft()
        peak_difficulty = mountain_peaks[next_peak]

        if stamina_consumed + food_consumed >= peak_difficulty:
            continue
        else:
            peaks_queue.appendleft(next_peak)
            continue

    # result message stating if the climber has managed to conquer all the peaks or not
    if peaks_queue:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        if len(peaks_queue) != len(mountain_peaks):
            print("Conquered peaks:")
            {print(key) for key in mountain_peaks.keys() if key not in peaks_queue}

    else:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        print("Conquered peaks:")
        {print(key) for key in mountain_peaks.keys()}


if __name__ == "__main__":
    main()
