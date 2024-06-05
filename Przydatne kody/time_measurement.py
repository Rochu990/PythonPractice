import time


def measurement(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    total_time = end - start
    return total_time


def multiply(a, b):
    return a * b


print(measurement(multiply, 125647, [1, 23, 4, 5, 6, 77, 8, 9, 7]))
