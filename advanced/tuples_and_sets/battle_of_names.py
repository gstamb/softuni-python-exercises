def get_ascii_sum(name_str: str) -> int:
    val = sum([ord(x) for x in name_str])
    return val


def print_results(odd_vals: set, even_vals: set):
    if sum(odd_vals) == sum(even_vals):
        common_vals = odd_vals.union(even_vals)
        print(f"{', '.join([str(x) for x in common_vals])}")
    elif sum(odd_vals) > sum(even_vals):
        odd_only_vals = odd_vals.difference(even_vals)
        print(f"{', '.join([str(x) for x in odd_only_vals])}")
    else:
        symmetric_diff_vals = odd_vals.symmetric_difference(even_vals)
        print(f"{', '.join([str(x) for x in symmetric_diff_vals])}")


def main():
    name_odd_ascii_val = set()
    name_even_ascii_val = set()

    for index in range(1, int(input()) + 1):
        name = input()
        ascii_val = get_ascii_sum(name)
        final_val = ascii_val // index
        if final_val % 2 == 0:
            name_even_ascii_val.add(final_val)
        else:
            name_odd_ascii_val.add(final_val)

    print_results(name_odd_ascii_val, name_even_ascii_val)


if __name__ == "__main__":
    main()
