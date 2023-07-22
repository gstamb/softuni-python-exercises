def main():
    first_set_len, second_set_len = map(int, input().split())
    first_set = set([input() for x in range(first_set_len)])
    second_set = set([input() for x in range(second_set_len)])

    intersect = first_set.intersection(second_set)
    print('\n'.join(intersect))


if __name__ == "__main__":
    main()
