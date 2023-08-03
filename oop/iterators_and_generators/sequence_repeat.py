class SequenceRepeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            current_index = self.counter % len(self.sequence)
            current_char = self.sequence[current_index]
            self.counter += 1
            return current_char

        else:
            raise StopIteration
