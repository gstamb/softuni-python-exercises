def read_next(*args):
    index = 0
    while index <= len(args) - 1:
        for item in args[index]:
            yield item
        index += 1
