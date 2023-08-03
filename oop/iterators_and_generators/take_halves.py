def solution():
    def integers():
        index = 1
        while True:
            yield index
            index += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
