from collections import deque


def find_colors(substrings, main_colors, secondary_colors):
    found_colors = []
    while substrings:
        if len(substrings) > 1:
            left = substrings.popleft()
            right = substrings.pop()
            string = left + right
            reversed_string = right + left
            if string in main_colors or string in secondary_colors:
                found_colors.append(string)
                continue
            # reverse check required for it to pass the tests
            if reversed_string in main_colors or reversed_string in secondary_colors:
                found_colors.append(reversed_string)
                continue
            else:
                # remove last elements of each substring and insert in the middle of the queue
                left = left[:-1]
                right = right[:-1]
                mid_index = len(substrings) // 2
                # variation of index depending on odd even length as per instruction
                if len(substrings) % 2 == 1:
                    mid_index = (len(substrings) - 1) // 2

                if right:
                    substrings.insert(mid_index, right)
                if left:
                    substrings.insert(mid_index, left)

        else:
            whole = substrings.pop()
            if whole in main_colors or whole in secondary_colors:
                found_colors.append(whole)

    return found_colors


def filter_colors(required_colors, colors):
    """ Filters secondary colors that do not have the composing main colors in the result """
    result_colors = set(colors)
    for color in result_colors:
        if color in required_colors:
            if result_colors.intersection(required_colors[color]) == required_colors[color]:
                pass
            else:
                colors.remove(color)


def main():
    substrings = deque(input().split())
    main_colors = ["red", "yellow", "blue"]
    secondary_colors = ["orange", "purple", "green"]
    required_colors = {"orange": {"red", "yellow"},
                       "purple": {"red", "blue"},
                       "green": {"yellow", "blue"}}

    # find all colors contained in the substrings
    colors = find_colors(substrings, main_colors, secondary_colors)

    # only keeps secondary colors that are a composite of main colors found
    filter_colors(required_colors, colors)

    print(colors)


if __name__ == "__main__":
    main()
