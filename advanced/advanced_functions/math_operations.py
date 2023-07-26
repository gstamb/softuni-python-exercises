def math_operations(*args: float, **kwargs):
    """
    Perform math operations of operands received from positional and key-value arguments
    :param args: float point numbers to serve as operands
    :param kwargs: key-value pairs. Key contain a specific mathematical operation and the value contain an operand.
                   - Key "a" represents addition.
                   - Key "s" represents subtraction.
                   - Key "d" represents division. (Note: Division by zero is handled.)
                   - Key "m" represents multiplication.
    :return:A string containing the result after all mathematical operations have been performed.
    """

    result_str = ""
    for index, argument in enumerate(args):
        position_in_kwargs = index % len(kwargs)
        if position_in_kwargs == 0:
            kwargs["a"] += argument
        elif position_in_kwargs == 1:
            kwargs["s"] -= argument
        elif position_in_kwargs == 2:
            if argument == 0:
                continue
            kwargs["d"] = kwargs["d"] / argument
        elif position_in_kwargs == 3:
            kwargs["m"] = kwargs["m"] * argument

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result_str += f"{key}: {value:.1f}\n"
    return result_str


def main():
    print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))


if __name__ == "__main__":
    main()
