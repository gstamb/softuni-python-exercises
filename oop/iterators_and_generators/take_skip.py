class TakeSkip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        max_printable = (self.count - 1) * self.step
        if self.current_number > max_printable:
            raise StopIteration

        value = self.current_number
        self.current_number += self.step
        return value


