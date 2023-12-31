import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arguments = args
        return_string = f"you called {func.__name__}{args}\n"
        result = func(*args, **kwargs)
        return_string += f"it returned {result}"
        return return_string

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
