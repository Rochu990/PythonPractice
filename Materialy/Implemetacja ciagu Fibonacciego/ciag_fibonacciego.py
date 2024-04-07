# source: https://ddeby.pl/blog/implementacja-ciagu-fibonacciego-w-python


def fib(n):
    result = [1, 1]
    for i in range(n - 2):
        result.append(result[i] + result[i + 1])
    return result


print(fib(10))


def rec_fib(n):
    if n < 2:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)


def fibb(n):
    return (rec_fib(a) for a in range(n))

class FibIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a
