class IncrementIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        return self.i


for i, num in enumerate(IncrementIterator(3)):
    print(i, num)