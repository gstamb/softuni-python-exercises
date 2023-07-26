def func_executor(*tuples):
    """
    Receives a tuple of tuples containing a list of functions and arguments. Executes the functions. Prints the results.
    :param args: number of arguments containing functions and arguments
    :return: a string containing the execution results of each function
    """
    executed_functions_results = ""
    for func, args in tuples:
        result = func(*args)
        executed_functions_results += f"{func.__name__} - {result}\n"

    return executed_functions_results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def main():
    print(func_executor(
        (sum_numbers, (1, 2)),
        (multiply_numbers, (2, 4))
    ))


if __name__ == "__main__":
    main()
