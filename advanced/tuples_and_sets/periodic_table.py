def main():
    elements_set = set()
    for seq in range(int(input())):
        elements = input()
        [elements_set.add(x) for x in elements.split()]

    print('\n'.join(elements_set))


if __name__ == "__main__":
    main()
