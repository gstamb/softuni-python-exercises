import functools


def cache(func):
    func.log = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args[0]
        if cache_key not in func.log:
            value = func(*args, **kwargs)
            func.log[cache_key] = value
        return func.log[cache_key]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
