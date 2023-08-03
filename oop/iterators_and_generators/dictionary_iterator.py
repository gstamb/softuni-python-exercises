class DictionaryIter:
    def __init__(self, dictionary_obj):
        self.dictionary = dictionary_obj
        self.keys = list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        max_index = len(self.keys) - 1
        if self.index > max_index:
            raise StopIteration
        key = self.keys[self.index]
        value = self.dictionary[key]
        self.index += 1
        return key, value
