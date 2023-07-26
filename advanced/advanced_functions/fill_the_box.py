def fill_the_box(*args):
    """
    Fill in the container with boxes until it runs out of space.
    :param args: First 3 digits represent the dimensions (length, width, height) of a container.
                 Next `N` digits represent the dimensions of boxes meant to fit into the container.
                 The arguments contain a string "Finish" that serves a delimeter between the current set of boxes the
                 next. It can appear anywhere in the string after the first three digits.
    :return: returns a string whether the container has been filled or more space is required
    """
    dimensions_of_container = list(args)[:3]
    boxes = list(args)[3:args.index("Finish")]
    space_taken_m3 = 0

    # calculate the available space
    available_space = dimensions_of_container[0]
    for dimensions in range(1, len(dimensions_of_container)):
        available_space *= dimensions_of_container[dimensions]

    # put boxes in the container
    for index, box in enumerate(boxes):
        # if next box will fill up the container, calculate additional space required to contain all the boxes
        if available_space < space_taken_m3 + box:
            left = boxes[index:]
            return f"No more free space! You have {sum(left) - (available_space - space_taken_m3)} more cubes."
        space_taken_m3 += box

    # all boxes are inside the container return additional space
    if available_space >= space_taken_m3:
        return f"There is free space in the box. You could put {available_space - space_taken_m3} more cubes."


def main():
    print(fill_the_box(2, 8,
                       2, 2, 1, 7, 3, 1, 5,
                       "Finish"))


if __name__ == "__main__":
    main()
