from typing import List


def get_total_racks(clothes: List[int], capacity: int) -> int:
    """Receives a list of clothes and rack capacity, returns the number of racks needed."""
    if not clothes:
        return 0

    racks = 1
    current_rack_load = 0

    for cloth in reversed(clothes):
        if current_rack_load + cloth > capacity:
            racks += 1
            current_rack_load = cloth
        else:
            current_rack_load += cloth

    return racks


def main():
    box_clothes = list(map(int, input().split()))
    rack_capacity = int(input())
    print(get_total_racks(box_clothes, rack_capacity))


if __name__ == "__main__":
    main()
