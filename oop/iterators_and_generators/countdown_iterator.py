class CountdownIterator:
    def __init__(self, count):
        self.count = count
        self.current_num = count
        self.minimum_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.minimum_num:
            raise StopIteration
        value = self.current_num
        self.current_num -= 1
        return value
