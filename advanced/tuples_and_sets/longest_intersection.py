def main():
    longest = set()
    for _ in range(int(input())):
        first, second = input().split("-")

        start, end = map(int, first.split(","))
        first_set = set([int(x) for x in range(int(start), int(end) + 1)])

        start, end = map(int, second.split(","))
        second_set = set([int(x) for x in range(int(start), int(end) + 1)])

        intersection = first_set.intersection(second_set)
        if len(intersection) > len(longest):
            longest = intersection

    print(f"Longest intersection is {list(longest)} with length {len(longest)}")


if __name__ == "__main__":
    main()
