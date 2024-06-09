import time

def timee(func, *args):
    def measurement():
        start = time.time()
        func(*args)
        end = time.time()
        total_time = end - start
        print(total_time)
    return measurement


@timee
def bubble(data):

    new_data = len(data)

    while new_data > 1:

        for i in range(0, new_data - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        new_data -= 1
        print(data)

    return data

digits = [1, 3, 6, 32, 6, 4, 5]
bubble(digits)